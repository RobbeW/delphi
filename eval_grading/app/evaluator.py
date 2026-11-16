"""Bounded interpreter for a deliberately small Python subset; never executes source."""
import ast
import math
import operator
import warnings

def parse_source(code):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore',SyntaxWarning)
        return ast.parse(code,filename='<inzending>')

class Unsupported(ValueError):
    pass

BIN = {ast.Add:operator.add, ast.Sub:operator.sub, ast.Mult:operator.mul, ast.Div:operator.truediv, ast.FloorDiv:operator.floordiv, ast.Mod:operator.mod, ast.Pow:operator.pow}
CMP = {ast.Eq:operator.eq, ast.NotEq:operator.ne, ast.Lt:operator.lt, ast.LtE:operator.le, ast.Gt:operator.gt, ast.GtE:operator.ge}

class Interpreter:
    def __init__(self, inputs):
        self.inputs = iter(inputs.splitlines()); self.vars = {}; self.output = ''; self.prompts = []; self.lines = []; self.steps = 0
        self.evaluated=set(); self.numeric_nodes=set(); self.derived_vars=set(); self.input_vars=set(); self.input_nodes=set(); self.controls=[]; self.prints=[]; self.calculations=[]
    def input_dependent(self,n):
        return any(id(x) in self.evaluated and ((isinstance(x,ast.Name) and x.id in self.input_vars) or id(x) in self.input_nodes) for x in ast.walk(n))
    def calculated(self,n):
        if isinstance(n,ast.FormattedValue):return self.calculated(n.value)
        if id(n) not in self.evaluated:return False
        if isinstance(n,ast.Name):return n.id in self.derived_vars
        if id(n) in self.numeric_nodes:return True
        return any(self.calculated(x) for x in ast.iter_child_nodes(n))
    def assign(self,name,value,node):
        derived=self.calculated(node) or any(self.controls)
        dependent=self.input_dependent(node) or any(self.controls)
        self.vars[name]=value
        (self.derived_vars.add if derived else self.derived_vars.discard)(name)
        (self.input_vars.add if dependent else self.input_vars.discard)(name)
    def tick(self):
        self.steps += 1
        if self.steps > 3000: raise Unsupported('stappenlimiet')
    def bounded(self, v):
        if isinstance(v, (int, float)) and (abs(v) > 1e12 or not math.isfinite(v)): raise Unsupported('getallimiet')
        if isinstance(v, str) and len(v) > 10000: raise Unsupported('tekstlimiet')
        return v
    def expr(self, n):
        self.tick()
        self.evaluated.add(id(n))
        if isinstance(n, ast.Tuple): return tuple(self.expr(x) for x in n.elts)
        if isinstance(n, ast.JoinedStr):
            parts=[]
            for part in n.values:
                if isinstance(part, ast.Constant) and isinstance(part.value,str): parts.append(part.value)
                elif isinstance(part, ast.FormattedValue) and part.conversion in (-1,115,114,97):
                    v=self.expr(part.value)
                    if part.format_spec is not None: raise Unsupported('formaatspecificatie')
                    parts.append(repr(v) if part.conversion==114 else ascii(v) if part.conversion==97 else str(v))
                else: raise Unsupported('f-string')
            return self.bounded(''.join(parts))
        if isinstance(n, ast.Constant) and type(n.value) in (int,float,str,bool,type(None)): return self.bounded(n.value)
        if isinstance(n, ast.Name) and n.id in self.vars: return self.vars[n.id]
        if isinstance(n, ast.BinOp) and type(n.op) in BIN:
            a, b = self.expr(n.left), self.expr(n.right)
            if isinstance(a,tuple) or isinstance(b,tuple): raise Unsupported('tuplebewerking')
            if isinstance(n.op,ast.Mod) and isinstance(a,str): raise Unsupported('tekstopmaak')
            if isinstance(n.op, ast.Pow) and (not isinstance(b, (int,float)) or abs(b) > 12): raise Unsupported('exponentlimiet')
            if isinstance(n.op, ast.Mult) and ((isinstance(a,str) and isinstance(b,int) and len(a)*abs(b)>10000) or (isinstance(b,str) and isinstance(a,int) and len(b)*abs(a)>10000)): raise Unsupported('tekstlimiet')
            value=self.bounded(BIN[type(n.op)](a,b))
            if type(value) in (int,float):
                self.numeric_nodes.add(id(n));self.calculations.append({'line':n.lineno,'column':n.col_offset,'operator':type(n.op).__name__})
            return value
        if isinstance(n, ast.UnaryOp):
            v=self.expr(n.operand)
            if isinstance(n.op, ast.Not): return not v
            if isinstance(n.op, ast.USub): return self.bounded(-v)
            if isinstance(n.op, ast.UAdd): return self.bounded(+v)
        if isinstance(n, ast.BoolOp):
            v=self.expr(n.values[0])
            for x in n.values[1:]:
                if isinstance(n.op, ast.And) and not v or isinstance(n.op, ast.Or) and v: break
                v=self.expr(x)
            return v
        if isinstance(n, ast.Compare):
            a=self.expr(n.left)
            for op, x in zip(n.ops,n.comparators):
                b=self.expr(x)
                if type(op) not in CMP: raise Unsupported('vergelijking')
                if not CMP[type(op)](a,b): return False
                a=b
            return True
        if isinstance(n, ast.Call) and not n.keywords:
            name=n.func.id if isinstance(n.func,ast.Name) else ('math.ceil' if isinstance(n.func,ast.Attribute) and isinstance(n.func.value,ast.Name) and n.func.value.id=='math' and n.func.attr=='ceil' and self.vars.get('math') == '<math>' else '')
            if name not in ('input','print','int','float','str','round','math.ceil','ceil'): raise Unsupported('aanroep')
            if name in self.vars and name not in ('math.ceil','ceil'): raise Unsupported('overschreven ingebouwde functie')
            if name=='ceil' and self.vars.get('ceil') != '<ceil>': raise Unsupported('aanroep')
            args=[self.expr(a) for a in n.args]
            if name=='input':
                if len(args)>1: raise Unsupported('input')
                # Input prompts are not judged as learner output.
                if args: self.prompts.append(str(args[0]))
                self.input_nodes.add(id(n))
                return next(self.inputs)
            if name=='print':
                self.prints.append({'line':n.lineno,'arguments':[{'value':v,'calculated':self.calculated(arg) or any(self.controls)} for arg,v in zip(n.args,args)]})
                self.write(' '.join(map(str,args))+'\n'); return None
            return self.bounded({'int':int,'float':float,'str':str,'round':round,'math.ceil':math.ceil,'ceil':math.ceil}[name](*args))
        raise Unsupported('expressie: '+type(n).__name__)
    def write(self,s):
        self.output += s
        if len(self.output)>10000: raise Unsupported('uitvoerlimiet')
    def statements(self, body):
        for n in body:
            self.tick()
            self.lines.append(n.lineno)
            if isinstance(n,ast.Expr): self.expr(n.value)
            elif isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name): self.assign(n.targets[0].id,self.expr(n.value),n.value)
            elif isinstance(n,ast.AnnAssign) and isinstance(n.target,ast.Name) and n.value is not None: self.assign(n.target.id,self.expr(n.value),n.value)
            elif isinstance(n,ast.AugAssign) and isinstance(n.target,ast.Name) and type(n.op) in BIN:
                a=self.vars[n.target.id]; b=self.expr(n.value)
                if isinstance(n.op,ast.Pow) and (not isinstance(b,(int,float)) or abs(b)>12): raise Unsupported('exponentlimiet')
                if isinstance(a,str) or isinstance(b,str): raise Unsupported('tekstbewerking')
                self.vars[n.target.id]=self.bounded(BIN[type(n.op)](a,b))
                self.derived_vars.add(n.target.id)
                if self.input_dependent(n.value):self.input_vars.add(n.target.id)
            elif isinstance(n,ast.If):
                condition=self.expr(n.test);self.controls.append(self.input_dependent(n.test))
                try:self.statements(n.body if condition else n.orelse)
                finally:self.controls.pop()
            elif isinstance(n,ast.Import) and len(n.names)==1 and n.names[0].name=='math' and n.names[0].asname is None: self.vars['math']='<math>'
            elif isinstance(n,ast.ImportFrom) and n.module=='math' and n.level==0 and len(n.names)==1 and n.names[0].name=='ceil' and n.names[0].asname is None: self.vars['ceil']='<ceil>'
            elif isinstance(n,ast.Pass): pass
            else: raise Unsupported('instructie: '+type(n).__name__)

def run(code, inputs=''):
    machine=None
    try:
        if len(code)>100000 or len(inputs)>10000: raise Unsupported('invoerlimiet')
        tree=parse_source(code)
        if sum(1 for _ in ast.walk(tree))>10000: raise Unsupported('syntaxboomlimiet')
        allowed=(ast.Module,ast.Expr,ast.Assign,ast.AnnAssign,ast.AugAssign,ast.If,ast.Import,ast.ImportFrom,ast.alias,ast.Pass,ast.Constant,ast.Name,ast.Load,ast.Store,ast.BinOp,ast.UnaryOp,ast.BoolOp,ast.Compare,ast.Call,ast.Attribute,ast.Tuple,ast.JoinedStr,ast.FormattedValue,ast.Add,ast.Sub,ast.Mult,ast.Div,ast.FloorDiv,ast.Mod,ast.Pow,ast.Not,ast.USub,ast.UAdd,ast.And,ast.Or,ast.Eq,ast.NotEq,ast.Lt,ast.LtE,ast.Gt,ast.GtE)
        for node in ast.walk(tree):
            if not isinstance(node,allowed): raise Unsupported('syntax: '+type(node).__name__)
            if isinstance(node,ast.Attribute) and not (isinstance(node.value,ast.Name) and node.value.id=='math' and node.attr=='ceil'): raise Unsupported('attribuut')
            if isinstance(node,ast.Call) and (node.keywords or not isinstance(node.func,(ast.Name,ast.Attribute)) or isinstance(node.func,ast.Name) and node.func.id not in ('input','print','int','float','str','round','ceil')): raise Unsupported('aanroep')
        machine=Interpreter(inputs); machine.statements(tree.body)
        return {'state':'ok','output':machine.output,'prompts':machine.prompts,'lines':machine.lines,'prints':machine.prints,'calculations':machine.calculations,'variables':{k:v for k,v in machine.vars.items() if v not in ('<math>','<ceil>')}}
    except (Exception, RecursionError) as exc:
        return {'state':'unsupported' if isinstance(exc, Unsupported) else 'error', 'detail':str(exc) if isinstance(exc,Unsupported) else type(exc).__name__, 'line':getattr(exc,'lineno',None),
                'output':machine.output if machine else '', 'lines':machine.lines if machine else [],
                'variables':{k:v for k,v in machine.vars.items() if v not in ('<math>','<ceil>')} if machine else {}}
