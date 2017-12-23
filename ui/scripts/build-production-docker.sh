echo "Installing node modules"
npm install

gulp build 

echo "Building Docker"
docker build -t scoreucsc/bassa:ui .
