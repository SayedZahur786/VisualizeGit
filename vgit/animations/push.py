#!/usr/bin/env python3
"""
Git Learning Automation System
A comprehensive tool to learn Git commands through interactive animations and practice
"""

import sys
import time
import random
import os
from typing import List, Dict, Any
from dataclasses import dataclass
from enum import Enum

class Color:
    """ANSI color codes for terminal output"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

class GitCommand(Enum):
    INIT = "init"
    ADD = "add"
    COMMIT = "commit"
    PUSH = "push"
    PULL = "pull"
    BRANCH = "branch"
    CHECKOUT = "checkout"
    MERGE = "merge"
    STATUS = "status"
    LOG = "log"

@dataclass
class Commit:
    hash: str
    message: str
    author: str
    timestamp: str

@dataclass
class Branch:
    name: str
    commits: List[Commit]
    is_current: bool = False

class GitRepository:
    """Simulated Git repository for learning purposes"""
    
    def __init__(self, name: str = "my-project"):
        self.name = name
        self.branches: Dict[str, Branch] = {}
        self.current_branch = "main"
        self.staged_files: List[str] = []
        self.working_files: List[str] = []
        self.remote_url = f"https://github.com/user/{name}.git"
        self.is_initialized = False
        
    def generate_commit_hash(self) -> str:
        """Generate a realistic-looking commit hash"""
        chars = "abcdef0123456789"
        return ''.join(random.choices(chars, k=7))
    
    def get_current_time(self) -> str:
        """Get current timestamp in Git format"""
        return time.strftime("%Y-%m-%d %H:%M:%S")

class GitAnimator:
    """Handles all animations and visual feedback"""
    
    def __init__(self, speed: float = 1.0):
        self.speed = speed
        self.delay = 0.5 / speed
    
    def typewriter(self, text: str, color: str = Color.WHITE):
        """Typewriter effect for text"""
        for char in text:
            sys.stdout.write(f"{color}{char}{Color.END}")
            sys.stdout.flush()
            time.sleep(0.03 / self.speed)
        print()
    
    def progress_bar(self, steps: int, description: str):
        """Animated progress bar"""
        bar_length = 30
        for i in range(steps + 1):
            progress = i / steps
            filled = int(bar_length * progress)
            bar = f"{'█' * filled}{'░' * (bar_length - filled)}"
            percent = int(progress * 100)
            
            sys.stdout.write(f"\r{Color.CYAN}{description}: {Color.GREEN}[{bar}] {percent}%{Color.END}")
            sys.stdout.flush()
            time.sleep(self.delay)
        print()
    
    def commit_flow(self, commit: Commit):
        """Animate commit creation"""
        print(f"\n{Color.YELLOW}Creating commit...{Color.END}")
        time.sleep(self.delay)
        
        # Show commit details
        print(f"{Color.GREEN}✓{Color.END} Commit {Color.BOLD}{commit.hash}{Color.END}")
        print(f"  Author: {Color.CYAN}{commit.author}{Color.END}")
        print(f"  Date: {commit.timestamp}")
        print(f"  Message: {Color.WHITE}{commit.message}{Color.END}")
        
        # Animated commit flow
        flow = ["Working Directory", "Staging Area", "Local Repository"]
        for i, stage in enumerate(flow):
            if i > 0:
                print(f"{Color.GREEN}    ↓{Color.END}")
            print(f"  {Color.BOLD}{stage}{Color.END}")
            time.sleep(self.delay)
    
    def push_animation(self, commits: int, remote: str, branch: str):
        """Enhanced push animation"""
        print(f"\n{Color.MAGENTA}Pushing {commits} commit(s) to {remote}/{branch}...{Color.END}")
        
        # Connection phase
        self.progress_bar(3, "Establishing connection")
        
        # Upload phase
        for i in range(commits):
            sys.stdout.write(f"\r{Color.CYAN}Uploading commit {i+1}/{commits} ")
            for j in range(3):
                sys.stdout.write(f"{Color.GREEN}→{Color.END}")
                sys.stdout.flush()
                time.sleep(self.delay / 3)
            
        print(f"\n{Color.GREEN}✓ Push completed successfully!{Color.END}")
        print(f"  → {Color.BLUE}{remote}/{branch}{Color.END}")
    
    def branch_visualization(self, repo: GitRepository):
        """Visualize branch structure"""
        print(f"\n{Color.BOLD}Repository: {repo.name}{Color.END}")
        print("Branch structure:")
        
        for branch_name, branch in repo.branches.items():
            current = "* " if branch_name == repo.current_branch else "  "
            color = Color.GREEN if branch_name == repo.current_branch else Color.WHITE
            
            print(f"{color}{current}{branch_name}{Color.END}")
            
            # Show recent commits
            recent_commits = branch.commits[-3:] if len(branch.commits) > 3 else branch.commits
            for commit in reversed(recent_commits):
                print(f"    {Color.YELLOW}{commit.hash}{Color.END} {commit.message}")

class GitLearningSystem:
    """Main learning system that combines repository simulation with animations"""
    
    def __init__(self):
        self.repo = GitRepository()
        self.animator = GitAnimator()
        self.lessons_completed = 0
        self.total_lessons = 10
    
    def welcome(self):
        """Welcome message and introduction"""
        welcome_text = f"""
{Color.BOLD}{Color.CYAN}🎓 Welcome to Git Learning Automation! 🎓{Color.END}

This interactive system will teach you Git through:
• Animated command demonstrations
• Hands-on practice exercises
• Real-time feedback and tips
• Progressive skill building

Let's start your Git journey!
"""
        print(welcome_text)
        time.sleep(2)
    
    def lesson_init(self):
        """Lesson 1: Repository Initialization"""
        print(f"\n{Color.BOLD}=== Lesson 1: Repository Initialization ==={Color.END}")
        self.animator.typewriter("Let's create your first Git repository!")
        
        print(f"\n{Color.YELLOW}$ git init{Color.END}")
        self.animator.progress_bar(5, "Initializing repository")
        
        # Simulate repository creation
        self.repo.is_initialized = True
        self.repo.branches["main"] = Branch("main", [], True)
        
        print(f"{Color.GREEN}✓ Initialized empty Git repository in ./{self.repo.name}/.git/{Color.END}")
        self.lessons_completed += 1
    
    def lesson_add_commit(self):
        """Lesson 2: Adding and Committing Files"""
        print(f"\n{Color.BOLD}=== Lesson 2: Adding and Committing Files ==={Color.END}")
        
        # Simulate file creation
        files = ["README.md", "main.py", "requirements.txt"]
        self.repo.working_files.extend(files)
        
        self.animator.typewriter("Files created in working directory:")
        for file in files:
            print(f"  {Color.CYAN}📄 {file}{Color.END}")
        
        print(f"\n{Color.YELLOW}$ git add .{Color.END}")
        self.animator.progress_bar(3, "Staging files")
        self.repo.staged_files = files.copy()
        
        print(f"\n{Color.YELLOW}$ git commit -m \"Initial commit\"{Color.END}")
        
        # Create and animate commit
        commit = Commit(
            hash=self.repo.generate_commit_hash(),
            message="Initial commit",
            author="Student <student@example.com>",
            timestamp=self.repo.get_current_time()
        )
        
        self.animator.commit_flow(commit)
        self.repo.branches["main"].commits.append(commit)
        self.lessons_completed += 1
    
    def lesson_branching(self):
        """Lesson 3: Branching and Merging"""
        print(f"\n{Color.BOLD}=== Lesson 3: Branching and Merging ==={Color.END}")
        
        print(f"\n{Color.YELLOW}$ git branch feature-auth{Color.END}")
        self.animator.typewriter("Creating new branch 'feature-auth'...")
        
        # Create new branch
        new_branch = Branch("feature-auth", self.repo.branches["main"].commits.copy())
        self.repo.branches["feature-auth"] = new_branch
        
        print(f"\n{Color.YELLOW}$ git checkout feature-auth{Color.END}")
        self.animator.typewriter("Switching to branch 'feature-auth'...")
        self.repo.current_branch = "feature-auth"
        
        # Add commits to feature branch
        feature_commits = [
            Commit(self.repo.generate_commit_hash(), "Add login functionality", 
                  "Student <student@example.com>", self.repo.get_current_time()),
            Commit(self.repo.generate_commit_hash(), "Add password validation", 
                  "Student <student@example.com>", self.repo.get_current_time())
        ]
        
        for commit in feature_commits:
            time.sleep(1)
            self.animator.commit_flow(commit)
            self.repo.branches["feature-auth"].commits.append(commit)
        
        self.animator.branch_visualization(self.repo)
        self.lessons_completed += 1
    
    def lesson_push(self):
        """Lesson 4: Pushing to Remote"""
        print(f"\n{Color.BOLD}=== Lesson 4: Pushing to Remote ==={Color.END}")
        
        self.animator.typewriter(f"Remote repository: {self.repo.remote_url}")
        
        print(f"\n{Color.YELLOW}$ git push origin {self.repo.current_branch}{Color.END}")
        
        current_branch = self.repo.branches[self.repo.current_branch]
        commit_count = len(current_branch.commits)
        
        self.animator.push_animation(commit_count, "origin", self.repo.current_branch)
        self.lessons_completed += 1
    
    def interactive_quiz(self):
        """Interactive quiz to test understanding"""
        print(f"\n{Color.BOLD}=== Quick Quiz ==={Color.END}")
        
        questions = [
            {
                "question": "What command initializes a new Git repository?",
                "options": ["a) git start", "b) git init", "c) git create", "d) git new"],
                "correct": "b",
                "explanation": "git init creates a new Git repository in the current directory."
            },
            {
                "question": "What's the correct order for adding and committing files?",
                "options": ["a) commit, then add", "b) add, then commit", "c) push, then add", "d) merge, then commit"],
                "correct": "b",
                "explanation": "Files must be staged with 'git add' before they can be committed with 'git commit'."
            }
        ]
        
        score = 0
        for i, q in enumerate(questions, 1):
            print(f"\n{Color.CYAN}Question {i}: {q['question']}{Color.END}")
            for option in q['options']:
                print(f"  {option}")
            
            answer = input(f"\n{Color.YELLOW}Your answer: {Color.END}").lower().strip()
            
            if answer == q['correct']:
                print(f"{Color.GREEN}✓ Correct!{Color.END}")
                score += 1
            else:
                print(f"{Color.RED}✗ Incorrect.{Color.END}")
            
            print(f"{Color.WHITE}Explanation: {q['explanation']}{Color.END}")
            time.sleep(2)
        
        print(f"\n{Color.BOLD}Quiz Score: {score}/{len(questions)}{Color.END}")
        return score
    
    def practice_mode(self):
        """Interactive practice mode"""
        print(f"\n{Color.BOLD}=== Practice Mode ==={Color.END}")
        self.animator.typewriter("Try executing Git commands yourself!")
        
        commands_to_practice = [
            ("git status", "Check the status of your repository"),
            ("git log --oneline", "View commit history in compact format"),
            ("git branch -a", "List all branches"),
            ("git diff", "Show changes in working directory")
        ]
        
        for cmd, description in commands_to_practice:
            print(f"\n{Color.CYAN}Practice: {cmd}{Color.END}")
            print(f"Description: {description}")
            
            input(f"{Color.YELLOW}Press Enter to simulate this command...{Color.END}")
            
            # Simulate command output
            if "status" in cmd:
                self.simulate_status()
            elif "log" in cmd:
                self.simulate_log()
            elif "branch" in cmd:
                self.simulate_branch_list()
            elif "diff" in cmd:
                self.simulate_diff()
    
    def simulate_status(self):
        """Simulate git status output"""
        print(f"{Color.GREEN}On branch {self.repo.current_branch}{Color.END}")
        print("Your branch is up to date with 'origin/main'.")
        print("\nnothing to commit, working tree clean")
    
    def simulate_log(self):
        """Simulate git log output"""
        current_branch = self.repo.branches[self.repo.current_branch]
        for commit in reversed(current_branch.commits[-5:]):
            print(f"{Color.YELLOW}{commit.hash}{Color.END} {commit.message}")
    
    def simulate_branch_list(self):
        """Simulate git branch -a output"""
        for branch_name in self.repo.branches.keys():
            current = "* " if branch_name == self.repo.current_branch else "  "
            color = Color.GREEN if branch_name == self.repo.current_branch else Color.WHITE
            print(f"{color}{current}{branch_name}{Color.END}")
    
    def simulate_diff(self):
        """Simulate git diff output"""
    print("diff --git a/main.py b/main.py")
    print("index 1234567..abcdefg 100644")
    print("--- a/main.py")
    print("+++ b/main.py")
    print(f"{Color.CYAN}@@ -1,3 +1,4 @@{Color.END}")
    print(" def main():")
    print('     print("Hello, World!")')
    print(f"{Color.GREEN}+    print('Welcome to Git!'){Color.END}")
    
    def show_progress(self):
        """Show learning progress"""
        progress = (self.lessons_completed / self.total_lessons) * 100
        print(f"\n{Color.BOLD}=== Your Progress ==={Color.END}")
        print(f"Lessons completed: {self.lessons_completed}/{self.total_lessons}")
        print(f"Progress: {progress:.1f}%")
        
        # Progress bar
        bar_length = 20
        filled = int(bar_length * (self.lessons_completed / self.total_lessons))
        bar = f"{'█' * filled}{'░' * (bar_length - filled)}"
        print(f"{Color.GREEN}[{bar}]{Color.END}")
    
    def run_full_course(self):
        """Run the complete learning course"""
        try:
            self.welcome()
            
            # Core lessons
            self.lesson_init()
            self.lesson_add_commit()
            self.lesson_branching()
            self.lesson_push()
            
            # Interactive elements
            quiz_score = self.interactive_quiz()
            self.practice_mode()
            
            # Final summary
            self.show_progress()
            
            print(f"\n{Color.BOLD}{Color.GREEN}🎉 Congratulations! 🎉{Color.END}")
            print(f"{Color.CYAN}You've completed the Git Learning Automation course!{Color.END}")
            
            if quiz_score >= 2:
                print(f"{Color.GREEN}Excellent quiz performance!{Color.END}")
            
            print(f"\n{Color.YELLOW}Next steps:{Color.END}")
            print("• Practice with real repositories")
            print("• Learn advanced Git features")
            print("• Explore Git workflows (GitFlow, GitHub Flow)")
            print("• Study collaborative development practices")
            
        except KeyboardInterrupt:
            print(f"\n\n{Color.YELLOW}Course interrupted. You can resume anytime!{Color.END}")
        except Exception as e:
            print(f"\n{Color.RED}An error occurred: {e}{Color.END}")

# Command-line interface
def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "--fast":
            # Fast mode for quick demonstration
            system = GitLearningSystem()
            system.animator.speed = 3.0
            system.run_full_course()
        elif sys.argv[1] == "--lesson":
            # Run specific lesson
            lesson_num = int(sys.argv[2]) if len(sys.argv) > 2 else 1
            system = GitLearningSystem()
            
            lessons = [
                system.lesson_init,
                system.lesson_add_commit, 
                system.lesson_branching,
                system.lesson_push
            ]
            
            if 1 <= lesson_num <= len(lessons):
                lessons[lesson_num - 1]()
            else:
                print(f"Lesson {lesson_num} not found. Available: 1-{len(lessons)}")
        else:
            print("Usage: python git_learning.py [--fast] [--lesson <number>]")
    else:
        # Normal interactive mode
        system = GitLearningSystem()
        system.run_full_course()


# Simple PushAnimation class for direct animation testing
class PushAnimation:
    def __init__(self, commits=1, remote='origin', branch='main', speed=1.0, files=None, message=None):
        self.commits = commits
        self.remote = remote
        self.branch = branch
        self.files = files if files is not None else ["main.py", "README.md"]
        self.message = message if message is not None else "Update project files"
        self.animator = GitAnimator(speed=speed)

    def loading_line(self, text, dots=3, color=Color.WHITE, delay=0.4):
        sys.stdout.write(f"{color}{text}{Color.END}")
        sys.stdout.flush()
        for i in range(dots):
            time.sleep(delay)
            sys.stdout.write(f"{color}.{Color.END}")
            sys.stdout.flush()
        print()

    def animate(self):
        # Step 1: Greet developer with loading effect
        self.loading_line("Hello Developer", dots=3, color=Color.CYAN, delay=0.5)
        time.sleep(0.7)
        self.loading_line("You finished your work", dots=3, color=Color.WHITE, delay=0.4)
        time.sleep(0.7)
        self.loading_line("Changed files detected", dots=3, color=Color.YELLOW, delay=0.4)
        for file in self.files:
            self.loading_line(f"  • {file}", dots=2, color=Color.CYAN, delay=0.3)
        time.sleep(0.7)
        self.loading_line("Commit message added", dots=3, color=Color.YELLOW, delay=0.4)
        self.loading_line(f"  " + self.message, dots=2, color=Color.WHITE, delay=0.3)
        time.sleep(1)

        # Step 2: Commit staged
        self.loading_line("Commit created and staged locally", dots=4, color=Color.GREEN, delay=0.3)
        time.sleep(0.8)
        self.loading_line("Ready to push to remote repository", dots=4, color=Color.MAGENTA, delay=0.3)
        time.sleep(1)

        # Step 3: Begin push animation
        self.loading_line("Preparing to push", dots=5, color=Color.CYAN, delay=0.25)
        self.animator.progress_bar(2, "Preparing to push")
        time.sleep(0.5)
        self.loading_line("Establishing connection", dots=5, color=Color.YELLOW, delay=0.25)
        self.animator.progress_bar(3, "Establishing connection")
        time.sleep(0.7)

        # Step 4: Upload phase
        for i in range(self.commits):
            self.loading_line(f"Uploading commit {i+1}/{self.commits}", dots=3, color=Color.CYAN, delay=0.3)
            sys.stdout.write(f"  ")
            for j in range(3):
                sys.stdout.write(f"{Color.GREEN}→{Color.END}")
                sys.stdout.flush()
                time.sleep(self.animator.delay / 2)
            print()
        time.sleep(0.7)
        self.loading_line("Push completed successfully", dots=4, color=Color.GREEN, delay=0.3)
        print(f"  → {Color.BLUE}{self.remote}/{self.branch}{Color.END}")

if __name__ == "__main__":
    main()