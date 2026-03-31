# GitHub Activity CLI

A simple command line tool to fetch and display recent GitHub activity for any user.

## Requirements
- Python 3.x
- No external libraries needed

## Usage
```
python github_activity.py <username>
```

## Example
```
python github_activity.py kamranahmedse
```

## Example Output
```
Pushed commits to kamranahmedse/diffity
Commented on an issue in kamranahmedse/diffity
Opened a pull request in kamranahmedse/diffity
Opened an issue in kamranahmedse/diffity
```

## Error Handling
- If no username is provided → shows usage message
- If username does not exist → shows friendly error message
- If API fails → shows error message
