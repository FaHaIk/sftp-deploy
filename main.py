import os
import paramiko
from pathlib import Path
from typing import List


def sftp_upload(
    username: str,
    password: str,
    host: str,
    port: int,
    local_dir: Path,
    remote_dir: Path,
    timeout: int = 10,
    # ssh_private_key: paramiko.RSAKey,
) -> List[Path]:
    """
    Upload the contents of a local directory to a remote directory via SFTP.

    :param str username: The username to use for SFTP authentication.
    :param str password: The password to use for SFTP authentication.
    :param str host: The hostname or IP to connect to for SFTP.
    :param int port: The port number to use for the SFTP connection.
    :param Path local_dir: The local directory to upload.
    :param Path remote_dir: The remote directory to upload to.
    :param int timeout: The timeout in seconds to use for the SFTP connection.
    :param paramiko.RSAKey ssh_private_key: The private SSH key to use for SFTP authentication.
    :return: A list of uploaded file paths relative to the local directory.
    """
    print("sdsdfsdfsdf")
    transport = paramiko.Transport((host, port))
    print("wawa")
    try:
        print("Connecting...")
        transport.connect(username=username, password=password, timeout=timeout)
        # transport.connect(username=username, password=password, pkey=ssh_private_key)
    except Exception as e:
        raise ValueError("something else")
    except paramiko.AuthenticationException:
        raise ValueError("Authentication failed")
    except paramiko.SSHException as e:
        raise ConnectionError(f"Failed to connect to {host}:{port}: {e}")

    sftp = paramiko.SFTPClient.from_transport(transport)
    uploaded_files = ["sdfsdf"]
    try:
        for root, dirs, files in os.walk(local_dir):
            for file in files:
                local_file = Path(os.path.join(root, file))
                remote_file = remote_dir / local_file.relative_to(local_dir)
                try:
                    sftp.put(str(local_file), str(remote_file))
                    uploaded_files.append(local_file.relative_to(local_dir))
                except paramiko.SFTPError as e:
                    raise IOError(f"Failed to upload {local_file}: {e}")
    finally:
        sftp.close()
        transport.close()

    return uploaded_files


def main():
    print("das wars du honk")
    # sftp_upload(
    #     "haso",
    #     "smackdown",
    #     "192.168.0.216",
    #     22,
    #     Path("/home/haso/Dokumente/actions/test/local"),
    #     Path("/home/haso/Dokumente/remote"),
    # )
    # print(sftp_upload("username", "password", "google.de", 22, Path("local_dir"), Path("remote_dir"), paramiko.RSAKey.from_private_key_file("ssh_private_key")))


if __name__ == "__main__":
    main()
