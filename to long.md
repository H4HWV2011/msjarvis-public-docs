INFO:     172.18.0.62:33602 - "POST /chat HTTP/1.1" 200 OK
INFO:__main__:💬 Query: Who are you?...
INFO:__main__:🌟 Processing 21 models sequentially via proxies...
INFO:__main__:   [1/21] Processing TinyLlama...
INFO:httpx:HTTP Request: POST http://llm1-proxy:8201/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ TinyLlama: 299 chars via http://llm1-proxy:8201/generate
INFO:__main__:   [2/21] Processing Gemma...
INFO:httpx:HTTP Request: POST http://llm2-proxy:8202/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Gemma: 277 chars via http://llm2-proxy:8202/generate
INFO:__main__:   [3/21] Processing Phi3 Mini...
INFO:httpx:HTTP Request: POST http://llm10-proxy:8210/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Phi3 Mini: 486 chars via http://llm10-proxy:8210/generate
INFO:__main__:   [4/21] Processing Orca-Mini...
INFO:httpx:HTTP Request: POST http://llm13-proxy:8213/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Orca-Mini: 107 chars via http://llm13-proxy:8213/generate
INFO:__main__:   [5/21] Processing Dolphin-Phi...
INFO:httpx:HTTP Request: POST http://llm12-proxy:8212/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Dolphin-Phi: 490 chars via http://llm12-proxy:8212/generate
INFO:__main__:   [6/21] Processing Neural-Chat...
INFO:httpx:HTTP Request: POST http://llm17-proxy:8217/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Neural-Chat: 428 chars via http://llm17-proxy:8217/generate
INFO:__main__:   [7/21] Processing OpenChat...
INFO:httpx:HTTP Request: POST http://llm18-proxy:8218/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ OpenChat: 248 chars via http://llm18-proxy:8218/generate
INFO:__main__:   [8/21] Processing Zephyr...
INFO:httpx:HTTP Request: POST http://llm15-proxy:8215/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Zephyr: 428 chars via http://llm15-proxy:8215/generate
INFO:__main__:   [9/21] Processing Starling-LM...
INFO:httpx:HTTP Request: POST http://llm16-proxy:8216/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Starling-LM: 647 chars via http://llm16-proxy:8216/generate
INFO:__main__:   [10/21] Processing SQLCoder...
INFO:httpx:HTTP Request: POST http://llm6-proxy:8206/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ SQLCoder: 474 chars via http://llm6-proxy:8206/generate
INFO:__main__:   [11/21] Processing MedLlama2...
INFO:httpx:HTTP Request: POST http://llm3-proxy:8203/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ MedLlama2: 200 chars via http://llm3-proxy:8203/generate
INFO:__main__:   [12/21] Processing LLaVA...
INFO:httpx:HTTP Request: POST http://llm5-proxy:8205/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ LLaVA: 163 chars via http://llm5-proxy:8205/generate
INFO:__main__:   [13/21] Processing MiniCPM-V...
INFO:httpx:HTTP Request: POST http://llm4-proxy:8204/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ MiniCPM-V: 746 chars via http://llm4-proxy:8204/generate
INFO:__main__:   [14/21] Processing StarCoder2...
INFO:httpx:HTTP Request: POST http://llm7-proxy:8207/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ StarCoder2: 347 chars via http://llm7-proxy:8207/generate
INFO:__main__:   [15/21] Processing Vicuna...
INFO:httpx:HTTP Request: POST http://llm19-proxy:8219/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Vicuna: 100 chars via http://llm19-proxy:8219/generate
INFO:__main__:   [16/21] Processing LLaMA 3.1...
INFO:httpx:HTTP Request: POST http://llm22-proxy:8222/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ LLaMA 3.1: 617 chars via http://llm22-proxy:8222/generate
INFO:__main__:   [17/21] Processing Mistral...
INFO:httpx:HTTP Request: POST http://llm21-proxy:8221/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Mistral: 204 chars via http://llm21-proxy:8221/generate
INFO:__main__:   [18/21] Processing Qwen2...
INFO:httpx:HTTP Request: POST http://llm14-proxy:8214/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ Qwen2: 517 chars via http://llm14-proxy:8214/generate
INFO:__main__:   [19/21] Processing CodeLlama...
INFO:httpx:HTTP Request: POST http://llm8-proxy:8208/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ CodeLlama: 206 chars via http://llm8-proxy:8208/generate
INFO:__main__:   [20/21] Processing DeepSeek Coder...
INFO:httpx:HTTP Request: POST http://llm9-proxy:8209/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ DeepSeek Coder: 511 chars via http://llm9-proxy:8209/generate
INFO:__main__:   [21/21] Processing LLaMA 2...
INFO:httpx:HTTP Request: POST http://llm20-proxy:8220/generate "HTTP/1.1 200 OK"
INFO:__main__:✅ LLaMA 2: 415 chars via http://llm20-proxy:8220/generate
INFO:__main__:✅ Complete: 21/21 responded within budget (elapsed=262.5s)
INFO:     172.18.0.62:60302 - "POST /chat HTTP/1.1" 200 OK


cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ curl -sS -X POST "http://localhost:8050/ultimatechat" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: super-secret-key" \
  -d '{"message": "Who are you?", "userid": "cakidd", "role": "community"}' \
  | jq '{validated_by, consciousness_layers: (.consciousnesslayers | map({name: .name, status: .status}))}'
+ jq '{validated_by, consciousness_layers: (.consciousnesslayers | map({name: .name, status: .status}))}'
+ curl -sS -X POST http://localhost:8050/ultimatechat -H 'Content-Type: application/json' -H 'X-API-Key: super-secret-key' -d '{"message": "Who are you?", "userid": "cakidd", "role": "community"}'
		{
  "validated_by": null,
  "consciousness_layers": [
    {
      "name": "nbb-prefrontal-cortex",
      "status": "ok"
    },
    {
      "name": "qualia-engine",
      "status": "ok"
    },
    {
      "name": "consciousness-bridge",
      "status": "ok"
    },
    {
      "name": "neurobiological-master",
      "status": "ok"
    }
  ]
}
cakidd@cakidd-Legion-5-16IRX9:~/msjarvis-rebuild-working/msjarvis-rebuild$ + local cur prev words cword split
+ _init_completion -s
+ local exclude= flag outx errx inx OPTIND=1
+ getopts n:e:o:i:s flag -s
+ case $flag in
+ split=false
+ exclude+==
+ getopts n:e:o:i:s flag -s
+ COMPREPLY=()
+ local 'redir=@(?([0-9])<|?([0-9&])>?(>)|>&)'
+ _get_comp_words_by_ref -n '=<>&' cur prev words cword
+ local exclude flag i OPTIND=1
+ words=()
+ local cur cword words
+ upargs=()
+ upvars=()
+ local upargs upvars vcur vcword vprev vwords
+ getopts c:i:n:p:w: flag -n '=<>&' cur prev words cword
+ case $flag in
+ exclude='=<>&'
+ getopts c:i:n:p:w: flag -n '=<>&' cur prev words cword
+ [[ 6 -ge 3 ]]
+ case ${!OPTIND} in
+ vcur=cur
+ (( OPTIND += 1 ))
+ [[ 6 -ge 4 ]]
+ case ${!OPTIND} in
+ vprev=prev
+ (( OPTIND += 1 ))
+ [[ 6 -ge 5 ]]
+ case ${!OPTIND} in
+ vwords=words
+ (( OPTIND += 1 ))
+ [[ 6 -ge 6 ]]
+ case ${!OPTIND} in
+ vcword=cword
+ (( OPTIND += 1 ))
+ [[ 6 -ge 7 ]]
+ __get_cword_at_cursor_by_ref '=<>&' words cword cur
+ words=()
+ local cword words
+ __reassemble_comp_words_by_ref '=<>&' words cword
+ local exclude i j line ref
+ [[ -n =<>& ]]
+ exclude='[=<>&]'
+ printf -v cword %s -1
+ [[ -v exclude ]]
+ line=
+ (( i = 0, j = 0 ))
+ (( i < 0 ))
+ (( i == COMP_CWORD ))
+ local i cur= index=0 lead=
+ [[ 0 -gt 0 ]]
+ local words cword cur
+ _upvars -a0 words -v cword -1 -v cur ''
+ (( 8 ))
+ (( 8 ))
+ case $1 in
+ [[ -n 0 ]]
+ printf %d 0
+ [[ -n words ]]
+ unset -v words
+ eval 'words=("${@:3:0}")'
++ words=("${@:3:0}")
+ shift 2
+ (( 6 ))
+ case $1 in
+ [[ -n cword ]]
+ unset -v cword
+ eval 'cword="$3"'
++ cword=-1
+ shift 3
+ (( 3 ))
+ case $1 in
+ [[ -n cur ]]
+ unset -v cur
+ eval 'cur="$3"'
++ cur=
+ shift 3
+ (( 0 ))
+ [[ -v vcur ]]
+ upvars+=("$vcur")
+ upargs+=(-v $vcur "$cur")
+ [[ -v vcword ]]
+ upvars+=("$vcword")
+ upargs+=(-v $vcword "$cword")
+ [[ -v vprev ]]
+ [[ -1 -ge 1 ]]
+ [[ -v vwords ]]
+ upvars+=("$vwords")
+ upargs+=(-a${#words[@]} $vwords ${words+"${words[@]}"})
+ (( 3 ))
+ local cur cword words
+ _upvars -v cur '' -v cword -1 -a0 words
+ (( 8 ))
+ (( 8 ))
+ case $1 in
+ [[ -n cur ]]
+ unset -v cur
+ eval 'cur="$3"'
++ cur=
+ shift 3
+ (( 5 ))
+ case $1 in
+ [[ -n cword ]]
+ unset -v cword
+ eval 'cword="$3"'
++ cword=-1
+ shift 3
+ (( 2 ))
+ case $1 in
+ [[ -n 0 ]]
+ printf %d 0
+ [[ -n words ]]
+ unset -v words
+ eval 'words=("${@:3:0}")'
++ words=("${@:3:0}")
+ shift 2
+ (( 0 ))
+ _variables
+ [[ '' =~ ^(\$(\{[!#]?)?)([A-Za-z0-9_]*)$ ]]
+ [[ '' =~ ^(\$\{[#!]?)([A-Za-z0-9_]*)\[([^]]*)$ ]]
+ [[ '' =~ ^\$\{[#!]?[A-Za-z0-9_]*\[.*]$ ]]
+ return 1
+ [[ '' == @(?([0-9])<|?([0-9&])>?(>)|>&)* ]]
+ [[ '' == @(?([0-9])<|?([0-9&])>?(>)|>&) ]]
+ local i skip
+ (( i = 1 ))
+ (( i < 0 ))
+ (( cword <= 0 ))
+ return 1
+ return
+ local cur prev words cword split
+ _init_completion -s
+ local exclude= flag outx errx inx OPTIND=1
+ getopts n:e:o:i:s flag -s
+ case $flag in
+ split=false
+ exclude+==
+ getopts n:e:o:i:s flag -s
+ COMPREPLY=()
+ local 'redir=@(?([0-9])<|?([0-9&])>?(>)|>&)'
+ _get_comp_words_by_ref -n '=<>&' cur prev words cword
+ local exclude flag i OPTIND=1
+ words=()
+ local cur cword words
+ upargs=()
+ upvars=()
+ local upargs upvars vcur vcword vprev vwords
+ getopts c:i:n:p:w: flag -n '=<>&' cur prev words cword
+ case $flag in
+ exclude='=<>&'
+ getopts c:i:n:p:w: flag -n '=<>&' cur prev words cword
+ [[ 6 -ge 3 ]]
+ case ${!OPTIND} in
+ vcur=cur
+ (( OPTIND += 1 ))
+ [[ 6 -ge 4 ]]
+ case ${!OPTIND} in
+ vprev=prev
+ (( OPTIND += 1 ))
+ [[ 6 -ge 5 ]]
+ case ${!OPTIND} in
+ vwords=words
+ (( OPTIND += 1 ))
+ [[ 6 -ge 6 ]]
+ case ${!OPTIND} in
+ vcword=cword
+ (( OPTIND += 1 ))
+ [[ 6 -ge 7 ]]
+ __get_cword_at_cursor_by_ref '=<>&' words cword cur
+ words=()
+ local cword words
+ __reassemble_comp_words_by_ref '=<>&' words cword
+ local exclude i j line ref
+ [[ -n =<>& ]]
+ exclude='[=<>&]'
+ printf -v cword %s -1
+ [[ -v exclude ]]
+ line=
+ (( i = 0, j = 0 ))
+ (( i < 0 ))
+ (( i == COMP_CWORD ))
+ local i cur= index=0 lead=
+ [[ 0 -gt 0 ]]
+ local words cword cur
+ _upvars -a0 words -v cword -1 -v cur ''
+ (( 8 ))
+ (( 8 ))
+ case $1 in
+ [[ -n 0 ]]
+ printf %d 0
+ [[ -n words ]]
+ unset -v words
+ eval 'words=("${@:3:0}")'
++ words=("${@:3:0}")
+ shift 2
+ (( 6 ))
+ case $1 in
+ [[ -n cword ]]
+ unset -v cword
+ eval 'cword="$3"'
++ cword=-1
+ shift 3
+ (( 3 ))
+ case $1 in
+ [[ -n cur ]]
+ unset -v cur
+ eval 'cur="$3"'
++ cur=
+ shift 3
+ (( 0 ))
+ [[ -v vcur ]]
+ upvars+=("$vcur")
+ upargs+=(-v $vcur "$cur")
+ [[ -v vcword ]]
+ upvars+=("$vcword")
+ upargs+=(-v $vcword "$cword")
+ [[ -v vprev ]]
+ [[ -1 -ge 1 ]]
+ [[ -v vwords ]]
+ upvars+=("$vwords")
+ upargs+=(-a${#words[@]} $vwords ${words+"${words[@]}"})
+ (( 3 ))
+ local cur cword words
+ _upvars -v cur '' -v cword -1 -a0 words
+ (( 8 ))
+ (( 8 ))
+ case $1 in
+ [[ -n cur ]]
+ unset -v cur
+ eval 'cur="$3"'
++ cur=
+ shift 3
+ (( 5 ))
+ case $1 in
+ [[ -n cword ]]
+ unset -v cword
+ eval 'cword="$3"'
++ cword=-1
+ shift 3
+ (( 2 ))
+ case $1 in
+ [[ -n 0 ]]
+ printf %d 0
+ [[ -n words ]]
+ unset -v words
+ eval 'words=("${@:3:0}")'
++ words=("${@:3:0}")
+ shift 2
+ (( 0 ))
+ _variables
+ [[ '' =~ ^(\$(\{[!#]?)?)([A-Za-z0-9_]*)$ ]]
+ [[ '' =~ ^(\$\{[#!]?)([A-Za-z0-9_]*)\[([^]]*)$ ]]
+ [[ '' =~ ^\$\{[#!]?[A-Za-z0-9_]*\[.*]$ ]]
+ return 1
+ [[ '' == @(?([0-9])<|?([0-9&])>?(>)|>&)* ]]
+ [[ '' == @(?([0-9])<|?([0-9&])>?(>)|>&) ]]
+ local i skip
+ (( i = 1 ))
+ (( i < 0 ))
+ (( cword <= 0 ))
+ return 1
+ return


