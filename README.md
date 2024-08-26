# HitWicketAssignment

## Overview
This repository contains the complete codebase for the project, with clear separation between the client and server components. Each component has its own directory with its respective setup and run instructions.

## Repository Structure
- `client/`: Contains the front-end code.
- `server/`: Contains the back-end code.

## Prerequisites
Ensure you have the following installed on your machine:
- Node.js (for client setup)
- Python (for server setup)
- npm (Node Package Manager)
- Any additional dependencies as specified in the `requirements.txt` or `package.json` files.

## Setup Instructions

### Client Setup
1. Navigate to the client directory:
   ```bash
   cd client
   ```

2. Install the necessary dependencies:
   ```bash
   npm install
   ```

3. Run the client:
   ```bash
   npm start
   ```

4. The client will be accessible at:
   ```
   http://localhost:3000
   ```

### Server Setup
1. Navigate to the server directory:
   ```bash
   cd server
   ```

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   python app.py
   ```

4. The server will be running at:
   ```
   http://localhost:5000
   ```

## Running the Project
To run the entire project:
1. Start the server as per the instructions in the "Server Setup" section.
2. Start the client as per the instructions in the "Client Setup" section.
3. Navigate to `http://localhost:3000` to interact with the application.

## Contributing
Please read our [Contributing Guidelines](CONTRIBUTING.md) for more details on how to contribute to this project.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
