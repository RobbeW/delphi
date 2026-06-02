import json
import os
import random

random.seed(123456789)

evaldir = os.path.join("..", "evaluation")
if not os.path.exists(evaldir):
    os.makedirs(evaldir)


def write_json(data):
    with open(os.path.join(evaldir, "tests.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def write_yaml(data):
    lines = ["- tab: Feedback", "  contexts:"]

    for context in data["tabs"][0]["contexts"]:
        before_code = context["before"]["python"]["data"]
        testcase = context["testcases"][0]
        stdin = testcase["input"]["stdin"]["data"]
        stdout = testcase["output"]["stdout"]["data"]

        lines.extend(
            [
                "    -",
                "      before:",
                "        python:",
                "          data: " + json.dumps(before_code),
                "      testcases:",
                "        - stdin: " + json.dumps(stdin),
                "          stdout: " + json.dumps(stdout),
            ]
        )

    with open(os.path.join(evaldir, "tests.yaml"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


cases = [
    (7247, 8),
    (6507, 3),
    (6548, 5),
    (9833, 6),
    (3027, 1),
    (5147, 10),
    (9689, 12),
]

exportdata = {
    "tabs": [
        {
            "name": "Feedback",
            "contexts": [],
        }
    ]
}

for seed, beurten in cases:
    random.seed(seed)
    totaal = 0

    for _ in range(beurten):
        totaal += random.randint(1, 6)

    context = {
        "before": {
            "python": {
                "data": "import random; random.seed(" + str(seed) + ")",
            }
        },
        "testcases": [
            {
                "description": "Uitvoeren met seed "
                + str(seed)
                + " en invoer "
                + str(beurten)
                + " leidt tot:",
                "input": {
                    "stdin": {
                        "type": "text",
                        "data": str(beurten) + "\n",
                    }
                },
                "output": {
                    "stdout": {
                        "type": "text",
                        "data": "Na "
                        + str(beurten)
                        + " beurten zijn er "
                        + str(totaal)
                        + " besmettingen.\n",
                    }
                },
            }
        ],
    }

    exportdata["tabs"][0]["contexts"].append(context)

write_json(exportdata)
write_yaml(exportdata)
