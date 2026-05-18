# secretsdump-parser
Parses secretsdump output and extracts usernames with their NTLM hashes. 
Useful for quickly identifying credentials during post-exploitation.

## Usage
python parser.py

## Input / Output
Input: secretsdump output file (.txt)
Output: clean username : NTLM hash list

## Example Output
Administrator : 31d6cfe0d16ae931b73c59d7e0c089c0
Guest : 31d6cfe0d16ae931b73c59d7e0c089c0
Maks : 8846f7eaee8fb117ad06bdd830b7586c
