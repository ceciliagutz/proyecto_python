from pathlib import Path

import httpx


def download_file(url: str, destination: Path) -> None:
    """Downloand a file using streaming and save it to disk"""
    try:
        with httpx.Client(timeout=5.0) as client:
            with client.stream("GET", url) as response:
                response.raise_for_status()
                with destination.open("wb") as file:
                    for chunk in response.iter_bytes():
                        file.write(chunk)
        print("Download completed:", destination)

    except httpx.RequestError as e:
        print("Request error:", e)
    except httpx.HTTPStatusError as e:
        print("HTTP error:", e.response.status_code)


if __name__ == "__main__":
    url = "https://httpbin.org/image/png"
    output_path = Path("downloaded_image.png")

    download_file(url, output_path)
