# AWS Elastic Beanstalk Deployment Guide

## Prerequisites

1. Install AWS CLI and EB CLI:
```bash
pip install awsebcli
```

2. Configure AWS credentials:
```bash
aws configure
```

## Deployment Steps

### Method 1: Using EB CLI (Recommended)

1. **Initialize Elastic Beanstalk Application**
```bash
eb init -p python-3.11 demo-mcp-connector --region us-east-1
```

2. **Create Environment and Deploy**
```bash
eb create demo-mcp-env
```

3. **Open Application in Browser**
```bash
eb open
```

4. **Check Status**
```bash
eb status
```

5. **View Logs** (if issues occur)
```bash
eb logs
```

### Method 2: Using AWS Console

1. **Create Application Package**
```bash
# Remove any existing zip
rm -f application.zip

# Create zip with all necessary files
zip -r application.zip . -x "*.git*" "*__pycache__*" "*.pyc" ".elasticbeanstalk/*"
```

2. **Upload to AWS Console**
   - Go to AWS Elastic Beanstalk Console
   - Click "Create Application"
   - Choose "Python 3.11" platform
   - Upload `application.zip`
   - Configure instance type (t2.micro for testing)
   - Launch environment

## Configuration Changes Made

### 1. `app.py`
- Added `application = app` variable (EB requirement)
- Added health check endpoint at `/` for ELB health checks

### 2. `requirements.txt`
- Added version pins for reliable deployments
- Included all necessary dependencies

### 3. `Procfile`
- Specifies how to run the application
- Binds to correct port (8000)

### 4. `.ebextensions/01_python.config`
- Sets PYTHONPATH for proper imports
- Configures WSGI settings

### 5. `.ebignore`
- Excludes unnecessary files from deployment package

## Testing Your Deployment

Once deployed, test your endpoints:

```bash
# Get your EB URL
EB_URL=$(eb status | grep "CNAME" | awk '{print $2}')

# Test health check
curl http://$EB_URL/

# Test search accounts (with mock token)
curl -H "Authorization: mock-token" "http://$EB_URL/search_accounts?q=acme"

# Test get account details
curl -H "Authorization: mock-token" "http://$EB_URL/get_account_details/1"
```

## Common Issues and Solutions

### Issue 1: Application Not Starting
**Solution**: Check logs with `eb logs` to see specific error messages

### Issue 2: 502 Bad Gateway
**Cause**: Application not binding to correct port
**Solution**: Verify Procfile uses `--port 8000`

### Issue 3: Import Errors
**Cause**: Missing dependencies or incorrect PYTHONPATH
**Solution**: 
- Verify all dependencies in requirements.txt
- Check .ebextensions/01_python.config

### Issue 4: Health Check Failures
**Cause**: No endpoint at root `/`
**Solution**: Added health check endpoint at `/`

## Environment Variables

If you need to add environment variables:

```bash
# Using EB CLI
eb setenv VARIABLE_NAME=value

# Or in AWS Console
# Environment > Configuration > Software > Environment Properties
```

## Updating Your Application

```bash
# After making changes
eb deploy
```

## Monitoring

- **Logs**: `eb logs`
- **SSH into instance**: `eb ssh`
- **Health**: Check AWS Console > Elastic Beanstalk > Environment Health

## Cleanup (when done testing)

```bash
# Terminate environment
eb terminate demo-mcp-env

# This will stop billing for the resources
```

## Cost Optimization

For development/testing:
- Use t2.micro or t3.micro instances (free tier eligible)
- Use single instance environment (not load balanced)
- Terminate when not in use

## Security Considerations

1. **Authentication**: Currently uses mock token. For production:
   - Implement proper OAuth/JWT authentication
   - Use AWS Secrets Manager for tokens
   - Enable HTTPS only

2. **Environment Variables**: Store sensitive data in EB environment variables, not in code

3. **VPC**: Consider deploying in private subnet with NAT gateway for production

## Next Steps

1. Set up proper authentication
2. Configure custom domain name
3. Enable HTTPS with ACM certificate
4. Set up CloudWatch alarms
5. Configure auto-scaling (if needed)

