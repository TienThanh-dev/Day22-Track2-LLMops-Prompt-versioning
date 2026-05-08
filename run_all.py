"""Run all 4 steps sequentially, or a specific step with --step N."""
import argparse
import subprocess
import sys

STEPS = {
    1: "pseudocode/_01_langsmith_rag_pipeline.py",
    2: "pseudocode/02_prompt_hub_ab_routing.py",
    3: "pseudocode/03_ragas_evaluation.py",
    4: "pseudocode/04_guardrails_validator.py",
}

def main():
    parser = argparse.ArgumentParser(description="Run Day 22 lab steps")
    parser.add_argument("--step", type=int, choices=[1, 2, 3, 4],
                        help="Run a specific step (1-4)")
    args = parser.parse_args()

    steps_to_run = [args.step] if args.step else [1, 2, 3, 4]

    for step in steps_to_run:
        script = STEPS[step]
        print(f"\n{'='*60}")
        print(f"  Running Step {step}: {script}")
        print(f"{'='*60}\n")
        result = subprocess.run([sys.executable, script])
        if result.returncode != 0:
            print(f"❌ Step {step} failed with exit code {result.returncode}")
            sys.exit(result.returncode)
        print(f"✅ Step {step} completed\n")

    print(f"{'='*60}")
    print("  All steps completed successfully!")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()