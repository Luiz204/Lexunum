import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import parte1, parte2, parte3, parte4
dados = {}
for m in (parte1, parte2, parte3, parte4): dados.update(m.DADOS)
out = os.path.join(os.path.dirname(__file__), "..", "..", "doutrinas.json")
json.dump(dados, open(out, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(dados), "matérias,", sum(len(v) for v in dados.values()), "tópicos,", os.path.getsize(out), "bytes")

# Embute o JSON no index.html (funciona offline e sem servidor)
import re
idx = os.path.join(os.path.dirname(__file__), "..", "..", "index.html")
html = open(idx, encoding="utf-8").read()
bloco = json.dumps(dados, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
novo, n = re.subn(r'(<script type="application/json" id="doutrinasData">).*?(</script>)', lambda m: m.group(1) + bloco + m.group(2), html, count=1, flags=re.S)
assert n == 1, "marcador doutrinasData não encontrado"
open(idx, "w", encoding="utf-8").write(novo)
os.remove(out)
print("index.html atualizado")
