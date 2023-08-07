# Iris Biometrics Authentication Service

## Overview

This project implements an authentication service using Iris Biometrics, offering a cutting-edge way to securely manage user identities. Leveraging the unique patterns found in the iris, this system provides robust authentication and is suitable for various applications that require high security.

### Features

- **Registration of Clients**: Allows new applications to register and obtain client credentials.
- **Authentication Flows**: Implements different authentication flows to suit varying application needs.
- **Sequencer Endpoints**: Provides endpoints for the sequencer, enabling batching and proof verification.
- **Secure Token Handling**: Utilizes state and nonce parameters to prevent CSRF and replay attacks.
- **Iris Verification**: Facilitates user verification through Iris Biometrics, including signup handling for different environments.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- PostgreSQL 12 or higher
- Environment variables for client ID, redirect URI, etc.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-repo/iris-biometrics-authentication.git
   cd iris-biometrics-authentication
   ```

2. **Create a Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**:

   Create a `.env` file in the root directory and add the necessary variables:

   ```env
   CLIENT_ID=your_client_id
   REDIRECT_URI=https://app.example.com/login
   ```

5. **Run the Application**:

   ```bash
   uvicorn main:app --reload
   ```

   The application will be accessible at `http://localhost:8000`.

## Usage

### Registering a Client

- Endpoint: `POST /register`
- Payload: Application details including redirect URIs, client name, logo URL, etc.

### Starting Authentication

- Endpoint: `GET /start-auth`
- Redirects the user to the Iris Biometrics authentication page.

### Callback Handling

- Endpoint: `GET /login`
- Handles the redirected request after successful authentication.

### Sequencer Endpoints

- Various endpoints to interact with the sequencer for batching and proof verification.

[//]: # (## Contributing)

[//]: # ()
[//]: # (If you would like to contribute to this project, please follow the [CONTRIBUTING.md]&#40;CONTRIBUTING.md&#41; guidelines.)

[//]: # ()
[//]: # (## License)

[//]: # ()
[//]: # (This project is licensed under the MIT License - see the [LICENSE.md]&#40;LICENSE.md&#41; file for details.)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (Feel free to modify this README to align more closely with the specific details of your project.)