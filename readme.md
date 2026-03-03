# 🆔 RUT Generator

**Generador de RUTs chilenos válidos** para pruebas, diccionarios de ataque o testing de sistemas. 

## ✨ Características

- ✅ **RUTs válidos**: Calcula dígito verificador oficial chileno (K, 0-9)
- 🎨 **3 formatos**: `12345678-9`, `123456789`, `12345678` (sin DV)
- ⚡ **CLI intuitivo**: `python rutgen.py -c 1000 -f 1`
- 💾 **Exporta a archivo**: TXT con un RUT por línea
- 🛡️ **Sin duplicados**: Lista única garantizada

## 🚀 Instalación

```bash
git clone https://github.com/tuusuario/rut-generator.git
cd rut-generator
pip install -r requirements.txt  # Solo necesita Python stdlib
```

## 🚀 USO

# Generar 50 RUTs con guión (por defecto)
python rutgen.py

# 1000 RUTs sin guión, rango específico
python rutgen.py -c 1000 -f 2 -i 10000000 -e 25000000 -o diccionario.txt

# Rango completo (1M-40M), solo número base
python rutgen.py -c 5000 -f 3 -o ruts_sindv.txt
