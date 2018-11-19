from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = (b'gAAAAABb8mnkrfk0wIOQ5knX4A85NXrC1yODyxVSWz-B96oXCnqN0Vn9ZaKAZG'
           b'_BEbfrPqhI3a1bYnCcwkHwQxb6IcJwGTp5kN4hzD6XPcVSqmZAua2YSn3fsmrM'
           b'5qLEOG9LO3IAbs6aN77EuUJ1YxzcfUg7MG0JozWDTXRnV9v-kx00rRgcIMxJnv'
           b'VkXI9aN449Bw-Tx9nX')


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
