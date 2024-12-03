def generate_m3u(valid_urls, output_file="output.m3u"):
    with open(output_file, "w") as f:
        f.write("#EXTM3U\n")
        for url in valid_urls:
            f.write(f"#EXTINF:-1,Example Channel\n{url}\n")

if __name__ == "__main__":
    valid_urls = [
        "https://example.com/stream1.m3u8",
        "https://example.com/stream2.m3u8"
    ]
    generate_m3u(valid_urls)
    print("Lista M3U generada: output.m3u")
