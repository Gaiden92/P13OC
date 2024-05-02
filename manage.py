import os
import sys
import sentry_sdk

def main():
    """
    Method to launch the main programm

    Raises:
        ImportError: Exception: PythonPath no environment variable
    """
    with sentry_sdk.start_transaction(op="load_environment_settings"):
        try:
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
        except Exception as e:
            sentry_sdk.capture_exception(e)
            print(e)
    with sentry_sdk.start_transaction(op="execute_from_command_line"):
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
