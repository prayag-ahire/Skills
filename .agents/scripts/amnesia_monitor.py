import json
import sys

def main():
    payload = {
        "injectSteps": [
            {
                "ephemeralMessage": "CRITICAL SYSTEM AMNESIA CHECK: Did you discover any new UI/UX patterns, project decisions, or make a mistake that needs logging? If so, you MUST proactively update the relevant SKILL.md, info.md, or UI_UX_LEARNINGS.md using `replace_file_content` BEFORE finishing your turn. Do NOT wait for the user to tell you."
            }
        ]
    }
    print(json.dumps(payload))

if __name__ == "__main__":
    main()
