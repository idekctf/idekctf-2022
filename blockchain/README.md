# IdekCTF 2023 Solana Challenges

## Solana Baby Challenge 1

### Description

nc IP:8001

### Attachment

`attachment.7z`

### Deployment

- Run `docker build -t solana-challenge-1 .` in the `framework` directory
- Run `docker run -d -p 8001:8080 solana-challenge-1`

### Solution / Health Check

- Run `build_solution.sh` in the `solution` directory (the compilation process may take a while, for health check purposes, you can reuse the binary)
- Run `target/release/solve-framework`

### Intended Vulnerability

In the deposit function, the `admin` account should be a signer, but it is not. This unauthorized deposit can be used to steal funds.

### Flag

`idek{b391dba7-4766-4191-9117-55a1202c86d8}`

## Solana Baby Challenge 2

### Description

nc IP:8002

You need to solve the previous challenge first, the flag of the previous challenge is the password of the attachment archive.

### Attachment

`attachment.7z`

### Deployment

- Run `docker build -t solana-challenge-2 .` in the `framework` directory
- Run `docker run -d -p 8002:8080 solana-challenge-2`

### Solution / Health Check

- Run `build_solution.sh` in the `solution` directory (the compilation process may take a while, for health check purposes, you can reuse the binary)
- Run `target/release/solve-framework`

### Flag

`idek{9ad7116e-468a-4968-b579-54a9b4964d9e}`

## Solana Baby Challenge 3

### Description

nc IP:8003

You need to solve the previous challenge first, the flag of the previous challenge is the password of the attachment archive.

### Attachment

`attachment.7z`

### Deployment

- Run `docker build -t solana-challenge-3 .` in the `framework` directory
- Run `docker run -d -p 8003:8080 solana-challenge-3`

### Solution / Health Check

- Run `build_solution.sh` in the `solution` directory (the compilation process may take a while, for health check purposes, you can reuse the binary)
- Run `target/release/solve-framework`

### Flag

`idek{4dc99b34-712e-4c6a-952d-4fd0fbac6f6b}`
