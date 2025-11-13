# Troubleshooting: CNAME Unknown

## Step 1: Check Environment Status

```bash
eb status
```

Look for the environment status. It should show:

- **Creating**: Environment is still being set up (wait 5-10 minutes)
- **Ready**: Environment is healthy
- **Warning/Error**: There's a problem

## Step 2: Check Detailed Logs

```bash
# Get recent logs
eb logs

# Or get and save all logs
eb logs --all > eb_logs.txt
```

## Step 3: Check AWS Console

1. Go to AWS Elastic Beanstalk Console
2. Click on your application
3. Click on your environment
4. Check:
   - **Health**: Should be "Ok" (green)
   - **Recent Events**: Look for error messages
   - **Logs**: Request logs if needed

## Common Issues and Solutions

### Issue 1: Environment Still Creating

**Symptom**: CNAME shows as "unknown", status is "Launching"
**Solution**: Wait 5-10 minutes for initial environment creation

```bash
# Check status every minute
watch -n 60 eb status
```

### Issue 2: Python Version Mismatch

**Symptom**: Logs show "No module named 'app'" or import errors
**Solution**: Ensure correct Python version

```bash
# Reinitialize with specific Python version
eb init -p python-3.11 demo-mcp-connector --region us-east-1
```

### Issue 3: Port Configuration Issue

**Symptom**: 502 Bad Gateway, health checks failing
**Solution**: Verify port configuration

Check that Procfile uses port 8000:

```
web: uvicorn app:application --host 0.0.0.0 --port 8000
```

### Issue 4: Missing Dependencies

**Symptom**: Import errors in logs
**Solution**: Ensure all project files are included

```bash
# Verify files before deployment
eb deploy --staged

# Or manually check what's being uploaded
git ls-files
```

### Issue 5: WSGI Configuration

**Symptom**: Application not starting
**Solution**: Verify application variable exists

Make sure `app.py` has:

```python
application = app
```

## Step-by-Step Recovery

If your environment failed, try this:

### Option A: Terminate and Recreate

```bash
# 1. Terminate the problematic environment
eb terminate

# 2. Wait for termination to complete (check AWS console)

# 3. Recreate with more verbose output
eb create demo-mcp-env --verbose

# 4. Monitor logs in real-time
eb logs --stream
```

### Option B: Check Platform Version

```bash
# List available platforms
eb platform list

# Create with specific platform
eb create demo-mcp-env --platform "Python 3.11 running on 64bit Amazon Linux 2023"
```

### Option C: Manual Deployment via Console

1. **Create ZIP file**:

```bash
# Clean up first
rm -rf __pycache__ services/__pycache__ tools/__pycache__
rm -f application.zip

# Create clean deployment package
zip -r application.zip \
  app.py \
  requirements.txt \
  Procfile \
  .ebextensions/ \
  services/ \
  tools/ \
  mock_data.json \
  mcp.json \
  -x "*.pyc" "*__pycache__*" "*.git*" ".elasticbeanstalk/*"

# Verify contents
unzip -l application.zip
```

2. **Upload via AWS Console**:
   - Go to Elastic Beanstalk Console
   - Create new application
   - Choose **Python 3.11** platform
   - Upload `application.zip`
   - Configure:
     - Instance type: t2.micro (for testing)
     - Environment type: Single instance
   - Create environment

## Diagnostic Commands

```bash
# Check if EB is initialized
cat .elasticbeanstalk/config.yml

# Check current environment
eb list

# Get environment info
eb status --verbose

# Check health
eb health --refresh

# Stream logs in real-time
eb logs --stream
```

## Verify Local Setup First

Before deploying, test locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Test the application
uvicorn app:application --host 0.0.0.0 --port 8000

# In another terminal, test endpoints
curl http://localhost:8000/
curl -H "Authorization: mock-token" "http://localhost:8000/search_accounts?q=test"
```

## Check Deployment Package

Verify all required files are present:

```bash
# Required files checklist:
ls -la app.py                    # Main application
ls -la requirements.txt          # Dependencies
ls -la Procfile                  # Start command
ls -la .ebextensions/            # EB configuration
ls -la services/                 # Service modules
ls -la tools/                    # Tool modules
ls -la mock_data.json           # Mock data
```

## Get More Help

If still stuck, provide these details:

1. Output of `eb status`
2. Output of `eb logs` (last 50 lines)
3. Screenshot of AWS Console environment health
4. Region you're deploying to
5. Any error messages from Recent Events in console
