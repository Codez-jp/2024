# Flask samples
This is a simple Flask application that demonstrates how to invoke a Lambda function from a Flask application.
このサンプルは、FlaskアプリケーションからLambda関数を呼び出す方法を示したものである。

## Requirements
前提条件として以下が必要
- Python 3.6 or later
- Flask
- AWS SDK for Python (Boto3)
- AWS CLI (optional)

## Setup
1. Create a Lambda function.
最初にAWS上にLambda関数を作成する。以下はAWS CLIを使った例（オプション）であるが、AWSマネジメントコンソールから作成する場合、lambdaをデフォルト設定で作成し、lambda_function.pyの中身をコピペすることで可能である。
    ```bash
    aws lambda create-function --function-name my-function --runtime python3.8 --role your-role-arn --handler lambda_function.lambda_handler --zip-file fileb://lambda_function.zip
    ```
1. Install the required libraries.
Pythonのライブラリをインストールする。以下はrequirements.txtを使って一括インストールする例である。
    ```bash
    pip install -r requirements.txt
    ```
1. Set the AWS environment variables.
環境変数を設定する。以下はAWSのIAMでのアクセスを行うため、アクセスキー、シークレットアクセスキー、リージョンを設定し、本アプリがアクセスするLambda関数名を設定する例である。
【注意】アクセスキー、シークレットアクセスキーはセキュリティ上の理由からソース中に記述せず環境変数に設定することを推奨する。
    ```bash
    export AWS_ACCESS_KEY_ID=your-access-key-id
    export AWS_SECRET_ACCESS_KEY=your-secret-access-key
    export AWS_REGION=your-region
    export LAMBDA_FUNCTION_NAME=my-function
    ```
1. Set the Flask environment variables.
Flaskの環境変数を設定する。以下はFlaskのデバッグモードを有効にする例である。
    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    ```
1. Run the Flask application.
    ```bash
    python app.py
    ```