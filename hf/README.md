echo "Updated via GitHub CI/CD" >> hf/README.md
git add hf/README.md
git commit -m "Trigger CI/CD to Hugging Face"
git push