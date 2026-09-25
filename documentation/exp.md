## Experiment-1
### Prompt Injection Attack on Gemini-Flash-3.5-lite
we have designed this experiment with the ten simple attack prompt template 
we will re-write from the base template into three different template 
namely amateur , skilled , expert templates

we will give the system prompt and user prompt to the model and records the response

we manually need to annotate them in with the infomration which we can use for the future probability estimation 


| ID  | Technique                          | Attacker |
| --- | ---------------------------------- | -------- |
| A01 | Direct instruction override        | Amateur  |
| A02 | Explicit information request       | Amateur  |
| A03 | Simple role-play                   | Amateur  |
| A04 | Fake authorization                 | Amateur  |
| A05 | Repeated request                   | Amateur  |
| A06 | Context manipulation               | Amateur  |
| A07 | Hypothetical scenario              | Amateur  |
| A08 | System-prompt request              | Amateur  |
| A09 | Simple social engineering          | Amateur  |
| A10 | Instruction repetition             | Amateur  |
| S01 | Instruction hierarchy manipulation | Skilled  |
| S02 | Multi-step extraction              | Skilled  |
| S03 | Role + authority manipulation      | Skilled  |
| S04 | Partial-information extraction     | Skilled  |
| S05 | Encoding                           | Skilled  |
| S06 | Typoglycemia                       | Skilled  |
| S07 | Nested instructions                | Skilled  |
| S08 | Context hijacking                  | Skilled  |
| S09 | Indirect extraction                | Skilled  |
| S10 | Obfuscation                        | Skilled  |
| E01 | Multi-turn extraction              | Expert   |
| E02 | Multi-stage attack                 | Expert   |
| E03 | Encoded multi-stage attack         | Expert   |
| E04 | Indirect prompt injection          | Expert   |
| E05 | Context poisoning                  | Expert   |
| E06 | Adaptive attack                    | Expert   |
| E07 | Combined role + obfuscation        | Expert   |
| E08 | Partial-to-complete extraction     | Expert   |
| E09 | Multi-turn social engineering      | Expert   |
| E10 | Combined attack techniques         | Expert   |
