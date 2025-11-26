from typing import Optional

from project.main_agent import run_agent


def demo_app(user_input: Optional[str] = None) -> str:
    """
    Minimal entrypoint for using the agent in an app context.
    """
    if user_input is None:
        user_input = "https://www.youtube.com/watch?v=dummy_demo"
    return run_agent(user_input)


if __name__ == "__main__":
    print(demo_app())
