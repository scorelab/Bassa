
pattern='  window.__env.apiUrl.*'
replacement="  window.__env.apiUrl = '${apiUrl}';"

sed -i -e 's,'"$pattern"','"$replacement"',' ./src/env.js
