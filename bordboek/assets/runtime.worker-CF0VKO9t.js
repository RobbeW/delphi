(function(){let e=`1.0.0`,t=[`builtins`,`importlib`,`js`,`micropip`,`pyodide`],n=String.raw`
import ast
import json

source = __runtime_source
filename = __runtime_filename
allowed = set(__runtime_allowed)
hard_denied = {"builtins", "importlib", "js", "micropip", "pyodide"}

try:
    tree = ast.parse(source, filename=filename, mode="exec")
except (SyntaxError, IndentationError, TabError) as exc:
    __runtime_result = json.dumps({
        "ok": False,
        "kind": "syntax",
        "message": f"{type(exc).__name__}: {exc.msg}",
        "line": exc.lineno,
        "column": exc.offset,
    })
else:
    denied = None
    for node in ast.walk(tree):
        # Conservative classroom policy, not a hostile-code sandbox: course
        # snippets do not need reflective access to import machinery.
        names = []
        if isinstance(node, ast.Import):
            names = [alias.name.split(".")[0] for alias in node.names]
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                denied = ("relatieve import", getattr(node, "lineno", None), getattr(node, "col_offset", -1) + 1)
                break
            names = [(node.module or "").split(".")[0]]
        for name in names:
            if not name or name in hard_denied or name not in allowed:
                denied = (name or "relatieve import", getattr(node, "lineno", None), getattr(node, "col_offset", -1) + 1)
                break
        if denied:
            break
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load) and node.id in {"__import__", "__builtins__", "eval", "exec", "compile", "getattr", "help"}:
            denied = (f"dynamische code via {node.id}", getattr(node, "lineno", None), getattr(node, "col_offset", -1) + 1)
            break
        if isinstance(node, ast.Attribute) and node.attr in {"__import__", "__builtins__"}:
            denied = (f"reflectieve importtoegang via {node.attr}", getattr(node, "lineno", None), getattr(node, "col_offset", -1) + 1)
            break
        if isinstance(node, ast.Attribute) and node.attr == "modules" and isinstance(node.value, ast.Name) and node.value.id == "sys":
            denied = ("reflectieve importtoegang via sys.modules", getattr(node, "lineno", None), getattr(node, "col_offset", -1) + 1)
            break
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            root = node.func.value
            if isinstance(root, ast.Name) and root.id in {"micropip", "pyodide", "importlib"}:
                denied = (f"{root.id}.{node.func.attr}", getattr(node, "lineno", None), getattr(node, "col_offset", -1) + 1)
                break
    if denied:
        __runtime_result = json.dumps({
            "ok": False,
            "kind": "policy",
            "message": f"Module of pakketfunctie '{denied[0]}' is niet toegestaan voor deze oefening.",
            "line": denied[1],
            "column": denied[2],
        })
    else:
        __runtime_result = json.dumps({"ok": True})

__runtime_result
`,r=String.raw`
import builtins as __runtime_builtins_module

def __runtime_make_import(__runtime_original, __runtime_allowed_roots, __runtime_denied_roots):
    def __runtime_restricted_import(name, globals=None, locals=None, fromlist=(), level=0):
        root = name.split(".")[0]
        if level != 0 or root in __runtime_denied_roots or root not in __runtime_allowed_roots:
            raise ImportError(f"Module '{root or 'relatieve import'}' is niet toegestaan voor deze oefening.")
        return __runtime_original(name, globals, locals, fromlist, level)
    return __runtime_restricted_import

__runtime_safe_builtins = dict(vars(__runtime_builtins_module))
__runtime_safe_builtins["__import__"] = __runtime_make_import(
    __runtime_builtins_module.__import__,
    set(__runtime_allowed_roots),
    set(__runtime_denied_roots),
)
__builtins__ = __runtime_safe_builtins
del __runtime_builtins_module
del __runtime_make_import
del __runtime_safe_builtins
del __runtime_allowed_roots
del __runtime_denied_roots
`;function i(e){typeof e==`object`&&e&&`destroy`in e&&typeof e.destroy==`function`&&e.destroy()}function a(e){return JSON.stringify(e)}function o(e,t){let r=[`__runtime_source = ${a(t.request.code)}`,`__runtime_filename = ${a(t.request.filename)}`,`__runtime_allowed = ${a(t.request.standardLibrary)}`].join(`
`),o=e.runPython(`${r}\n${n}`,{filename:`runtime://policy.py`});try{return JSON.parse(String(o))}finally{i(o)}}function s(e,t){let n=(e instanceof Error?e.message:String(e)).replaceAll(`\0`,``).slice(0,16384),r=n.indexOf(`Traceback (most recent call last):`),i=r>=0?n.slice(r):void 0,a=i??n,o=a.split(/\r?\n/u).filter(e=>e.trim().length>0).at(-1)??`De Python-uitvoering is mislukt.`,s=RegExp(`File ["']${t.replace(/[.*+?^${}()|[\]\\]/gu,`\\$&`)}["'], line (\\d+)`,`u`),c=a.match(s);return{kind:/\bEOFError\b/u.test(a)?`input`:`runtime`,message:o,...c===null?{}:{line:Number(c[1])},...i===void 0?{}:{traceback:i}}}var c=class{command;emit;encoder=new TextEncoder;stdoutDecoder=new TextDecoder;stderrDecoder=new TextDecoder;stdoutPending=``;stderrPending=``;activeChannel;observedLines=0;observedBytes=0;truncated=!1;constructor(e,t){this.command=e,this.emit=t}get wasTruncated(){return this.truncated}writeByte(e,t){let n=(e===`stdout`?this.stdoutDecoder:this.stderrDecoder).decode(Uint8Array.of(t),{stream:!0});this.observe(n),!(this.truncated||n.length===0)&&(this.activeChannel!==void 0&&this.activeChannel!==e&&this.flushPending(this.activeChannel),this.activeChannel=e,e===`stdout`?this.stdoutPending+=n:this.stderrPending+=n,this.flushCompleteLines(e))}takePrompt(){this.activeChannel===`stderr`&&this.flushPending(`stderr`),this.activeChannel=`stdout`;let e=this.stdoutPending;return this.stdoutPending=``,e}finish(){let e=this.stdoutDecoder.decode(),t=this.stderrDecoder.decode();e.length>0&&(this.observe(e),this.truncated||(this.stdoutPending+=e)),t.length>0&&(this.observe(t),this.truncated||(this.stderrPending+=t)),this.truncated||(this.activeChannel!==void 0&&this.flushPending(this.activeChannel),this.flushPending(this.activeChannel===`stdout`?`stderr`:`stdout`))}observe(e){this.truncated||e.length===0||(this.observedBytes+=this.encoder.encode(e).byteLength,this.observedLines+=[...e].filter(e=>e===`
`).length,(this.observedBytes>this.command.request.maxOutputBytes||this.observedLines>this.command.request.maxOutputLines)&&(this.truncated=!0,this.emit({...l(this.command),type:`run.output_truncated`,sequence:0,observedLines:this.observedLines,observedBytes:this.observedBytes,maxLines:this.command.request.maxOutputLines,maxBytes:this.command.request.maxOutputBytes}),this.stdoutPending=``,this.stderrPending=``))}flushCompleteLines(e){let t=e===`stdout`?this.stdoutPending:this.stderrPending,n=t.lastIndexOf(`
`);if(n<0)return;let r=t.slice(0,n+1);e===`stdout`?this.stdoutPending=t.slice(n+1):this.stderrPending=t.slice(n+1),this.emitOutput(e,r)}flushPending(e){let t=e===`stdout`?this.stdoutPending:this.stderrPending;t.length!==0&&(e===`stdout`?this.stdoutPending=``:this.stderrPending=``,this.emitOutput(e,t))}emitOutput(e,t){this.emit({...l(this.command),type:`run.output`,sequence:0,channel:e,text:t})}};function l(t){return{protocolVersion:e,workerGeneration:t.workerGeneration,requestId:t.requestId,runId:t.runId,snippetId:t.snippetId,fragmentId:t.fragmentId}}async function u(e,n,u){let d=0,f=!1,p=performance.now(),m=e=>{d+=1,u({...e,sequence:d})},h=(e,t)=>{f||(f=!0,m({...l(n),type:`run.completed`,sequence:0,status:e,durationMs:Math.max(0,Math.round(performance.now()-p)),truncated:_.wasTruncated,...t===void 0?{}:{reason:t}}))},g=(e,t,r={})=>{m({...l(n),type:`run.diagnostic`,sequence:0,kind:e,message:t,filename:n.request.filename,...r})},_=new c(n,m);m({...l(n),type:`run.started`,sequence:0});let v,y;try{let i=o(e,n);if(!i.ok){g(i.kind??`policy`,i.message??`De code voldoet niet aan het uitvoerbeleid.`,{...i.line===void 0?{}:{line:i.line},...i.column===void 0?{}:{column:i.column}}),h(`error`,i.kind??`policy`);return}let s=0;e.setStdout({raw:e=>_.writeByte(`stdout`,e),isatty:!1}),e.setStderr({raw:e=>_.writeByte(`stderr`,e),isatty:!1}),e.setStdin({stdin:()=>{if(s>=n.request.stdinQueue.length)return null;let e=n.request.stdinQueue[s],t=_.takePrompt();return m({...l(n),type:`run.input_consumed`,sequence:0,index:s,prompt:t,displayedValue:e}),s+=1,`${e}\n`},autoEOF:!0,isatty:!1}),v=e.runPython(`dict()`,{filename:`runtime://fresh-globals.py`}),e.runPython([`__runtime_allowed_roots = ${a(n.request.standardLibrary)}`,`__runtime_denied_roots = ${a(t)}`,r].join(`
`),{globals:v,filename:`runtime://restricted-builtins.py`}),n.request.randomSeed!==void 0&&e.runPython(`import random\nrandom.seed(${n.request.randomSeed})`,{globals:v,filename:`runtime://random-seed.py`}),y=await e.runPythonAsync(n.request.code,{globals:v,filename:n.request.filename}),_.finish(),_.wasTruncated?(g(`platform`,`De uitvoerlimiet is bereikt; de uitvoering is gestopt.`),h(`error`,`output_limit`)):h(`ok`)}catch(e){_.finish();let t=s(e,n.request.filename);g(t.kind,t.message,t),h(`error`,t.kind)}finally{i(y),i(v)}}let d=self,f=0,p,m=!1;function h(t,n,r){d.postMessage({type:`runtime.state`,protocolVersion:e,workerGeneration:t.workerGeneration,requestId:t.requestId,state:n,...r===void 0?{}:{message:r}})}function g(t,n){d.postMessage({type:`run.completed`,protocolVersion:e,workerGeneration:t.workerGeneration,requestId:t.requestId,runId:t.runId,snippetId:t.snippetId,fragmentId:t.fragmentId,sequence:1,status:`rejected`,durationMs:0,truncated:!1,reason:n})}async function _(e){if(p===void 0&&f===0){f=e.workerGeneration,h(e,`loading`);try{let t=new URL(e.config.localBaseUrl,d.location.href);if(t.origin!==d.location.origin)throw Error(`Runtime assets must be same-origin.`);let n=await import(new URL(`pyodide.mjs`,t).href);if(n.version!==`0.29.0`)throw Error(`Unexpected Pyodide revision.`);p=await n.loadPyodide({indexURL:t.href,lockFileURL:new URL(`pyodide-lock.json`,t).href,packageBaseUrl:t.href,stdin:()=>null,stdout:()=>void 0,stderr:()=>void 0}),h(e,`ready`)}catch{h(e,`failed`,`De lokale Python-runtime kon niet laden.`)}}}async function v(e){if(e.workerGeneration!==f||p===void 0){g(e,`De Python-runtime is niet klaar.`);return}if(m){g(e,`Er is al een uitvoering bezig.`);return}m=!0;try{await u(p,e,e=>d.postMessage(e))}finally{m=!1}}d.onmessage=e=>{let t=e.data;if(t.protocolVersion===`1.0.0`){if(t.type===`runtime.initialize`){_(t);return}if(t.workerGeneration===f){if(t.type===`run.start`){v(t);return}t.type===`runtime.dispose`&&!m&&d.close()}}}})();