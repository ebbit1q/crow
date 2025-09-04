#!/bin/bash
target="$PWD/crow/pb"
cd "${BASH_SOURCE%/*}/" || exit 2
protoc="$PWD/protoc"
if [[ ! -x "$protoc" ]]; then
  protoc=protoc
  if ! hash "$protoc"; then
    echo "could not find protoc!" >&2
  fi
fi
tmp="$PWD/tmp"
pb_dir="common/pb"
src="$tmp/$pb_dir"
url="https://github.com/Cockatrice/Cockatrice"
if [[ ! -d $src ]]; then
  git clone --depth 1 --sparse --filter=blob:none "$url" "$tmp"
  { cd "$tmp" && git sparse-checkout set "$pb_dir" ; }
else
  { cd "$tmp" && git pull ; }
fi
mkdir -p "$target"
"$protoc" -I="$src" --python_out="$target" "$src"/*.proto
pyinit="__all__ = ["
xpyfile='^[^_].*\.py$'
n="
"
cd "$target" || exit 2
for file in *; do
  if [[ $file =~ $xpyfile ]]; then
    if [[ ! $yes ]]; then
      yes=1
      pyinit+="$n"
    else
      pyinit+=",$n"
    fi
    pyinit+="    '${file::-3}'"
  fi
done
if [[ ! $yes ]]; then
  echo "oop" >&2
  exit 1
fi
pyinit+="
]


def do_import():
    import sys
    import os
    import importlib
    this_dir = os.path.dirname(os.path.abspath(__file__))
    back = [*sys.path]
    sys.path.insert(0, this_dir)
    for name in __all__:
        globals()[name] = importlib.import_module(name)

    sys.path = back


do_import()"
cat >"__init__.py" <<<"$pyinit"
