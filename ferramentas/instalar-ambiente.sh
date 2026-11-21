#!/usr/bin/env bash
# Instala as linguagens e ferramentas usadas no repositório (Ubuntu/Debian).
# É o mesmo script usado pelo Codespaces (.devcontainer) e pelos testes automáticos (.github/workflows).
#
# Uso:
#   bash ferramentas/instalar-ambiente.sh             # linguagens + ferramentas de validação
#   bash ferramentas/instalar-ambiente.sh --geradores # também pandoc e bibliotecas Python dos geradores
#
# Só instala o que estiver faltando. Java e .NET normalmente já vêm do Codespaces/CI;
# se faltarem, o script instala o OpenJDK e o .NET 10.
set -euo pipefail

AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SUDO=""; [ "$(id -u)" -ne 0 ] && SUDO="sudo"
tem() { command -v "$1" >/dev/null 2>&1; }

pacotes=()
tem gcc     || pacotes+=(gcc)
tem g++     || pacotes+=(g++)
tem make    || pacotes+=(make)
tem php     || pacotes+=(php-cli)
tem perl    || pacotes+=(perl)
tem python3 || pacotes+=(python3)
tem pip3    || pacotes+=(python3-pip)
tem swipl   || pacotes+=(swi-prolog-nox)
tem curl    || pacotes+=(curl)
tem rlwrap  || pacotes+=(rlwrap)
tem java    || pacotes+=(default-jdk-headless)
if [ "${1:-}" = "--geradores" ]; then tem pandoc || pacotes+=(pandoc); fi

if [ ${#pacotes[@]} -gt 0 ]; then
  echo ">> apt: ${pacotes[*]}"
  $SUDO apt-get update -qq
  DEBIAN_FRONTEND=noninteractive $SUDO apt-get install -y -qq "${pacotes[@]}" >/dev/null
fi

# Clojure CLI (JVM) — instalador oficial: https://clojure.org/guides/install_clojure
if ! tem clojure; then
  echo ">> Clojure CLI"
  tmp="$(mktemp -d)"
  curl -fsSL -o "$tmp/linux-install.sh" https://github.com/clojure/brew-install/releases/latest/download/linux-install.sh
  chmod +x "$tmp/linux-install.sh"
  $SUDO "$tmp/linux-install.sh" >/dev/null
  rm -rf "$tmp"
fi
# baixa as dependências do Clojure uma vez (a primeira execução é mais lenta)
clojure -M -e '(println "Clojure" (clojure-version))' >/dev/null

# .NET SDK (C#)
if ! tem dotnet; then
  echo ">> .NET SDK 10"
  curl -fsSL -o /tmp/dotnet-install.sh https://dot.net/v1/dotnet-install.sh
  bash /tmp/dotnet-install.sh --channel 10.0 --install-dir "$HOME/.dotnet" >/dev/null
  $SUDO ln -sf "$HOME/.dotnet/dotnet" /usr/local/bin/dotnet
fi
export DOTNET_CLI_TELEMETRY_OPTOUT=1 DOTNET_NOLOGO=1

# Dependências Node (Mermaid, Tau-Prolog, nbb) e Python das ferramentas
if tem npm; then (cd "$AQUI" && npm ci --no-audit --no-fund --silent); fi
python3 -m pip install --quiet --user "bibtexparser<2" 2>/dev/null || python3 -m pip install --quiet --break-system-packages --user "bibtexparser<2"
if [ "${1:-}" = "--geradores" ]; then
  python3 -m pip install --quiet --user genanki markdown 2>/dev/null || python3 -m pip install --quiet --break-system-packages --user genanki markdown
fi

echo ">> Versões:"
gcc --version | head -1
g++ --version | head -1
java -version 2>&1 | head -1
dotnet --version | sed 's/^/.NET SDK /'
python3 --version
php --version | head -1
perl -e 'print "Perl $^V\n"'
clojure -M -e '(println "Clojure" (clojure-version))'
swipl --version
