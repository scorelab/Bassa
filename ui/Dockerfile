FROM node:latest



# Change directory so that our commands run inside this new directory
WORKDIR /Bassa/ui

# Copy dependency definitions
ADD . /Bassa/ui

# Install dependecies
RUN npm install


# Expose the port the app runs in
EXPOSE 4200

# Serve the app
CMD npm start