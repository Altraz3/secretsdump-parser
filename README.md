# secretsdump-parser
Parses secretsdump output and extracts NTLM-hashes

Parses secretsdump output and extracts usernames with their NTLM hashes. 
Useful for quickly identifying credentials during post-exploitation.

## Usage
python parser.py

## Input / Output
Input: secretsdump output file (.txt)
Output: clean username : NTLM hash list
