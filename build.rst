How to build
#########################################
mkdir -p pelican_themes
cd pelican_themes
git clone --recursive https://github.com/getpelican/pelican-themes pelican-themes
git clone git@github.com:mortada/pelican_javascript.git

pelican content
