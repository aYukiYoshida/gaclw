import argparse
import os
import shutil


def clean(folder_path: str) -> None:
    """
    指定されたディレクトリを削除する
    """
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        try:
            shutil.rmtree(folder_path)
        except Exception:
            return
    else:
        return


if __name__ == "__main__":
    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description="clean build artifacts")
    parser.add_argument(
        "folder_path", type=str, default="dist", help="path to folder to clean"
    )
    args = parser.parse_args()
    clean(args.folder_path)
