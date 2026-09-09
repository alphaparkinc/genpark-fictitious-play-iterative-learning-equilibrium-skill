"""MCP Server for Fictitious Play Skill."""
import json
import sys
from client import FictitiousPlay

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "run_fictitious_play",
                            "description": "Learn mixed Nash equilibrium via repeated fictitious play",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "p1_payoffs": {
                                        "type": "array",
                                        "items": {"type": "array", "items": {"type": "number"}}
                                    },
                                    "p2_payoffs": {
                                        "type": "array",
                                        "items": {"type": "array", "items": {"type": "number"}}
                                    },
                                    "iterations": {"type": "integer"}
                                },
                                "required": ["p1_payoffs", "p2_payoffs"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                fp = FictitiousPlay(args["p1_payoffs"], args["p2_payoffs"])
                out = fp.play(args.get("iterations", 500))
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(out)}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
