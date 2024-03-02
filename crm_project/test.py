# def fizzBuzz(n):
#     for num in range(1, n+1):
#         if num % 3 == 0 and num % 5 == 0:
#             print('FizzBuzz')
#         elif num % 3 == 0:
#             print('Fizz')
#         elif num % 5 == 0:
#             print('Buzz')
#         else:
#             print(num)

# fizzBuzz(15)

# lst = [5,1,3,11,9]
# szt = sorted(lst)
# # hg = sum(szt[:-1])

# from datetime import datetime

# def sort_and_filter_logs(logs):
#     # Filter logs for 'ERROR' and 'CRITICAL' severity
#     filtered_logs = [log for log in logs if log[2] in ('ERROR', 'CRITICAL')]

#     # Sort the filtered logs based on the extracted datetime values
#     sorted_logs = sorted(filtered_logs, key=lambda entry: datetime.strptime(f"{entry[0]} {entry[1]}", '%m-%d-%Y %H:%M'))

#     return sorted_logs

# # Example usage:
# logs = [['01-01-2023', '01:30', 'ERROR', 'failed'],
#         ['01-01-2023', '01:30', 'CRITICAL', 'failed'],
#         ['01-01-2023', '01:30', 'INFO', 'established']]

# filtered_and_sorted_logs = sort_and_filter_logs(logs)
# for log in filtered_and_sorted_logs:
#     print(log)


# def process_commands(expiry_limit, commands):
#     tokens = {}
#     for command in commands:
#         cmd_type, token_id, time = command
#         if cmd_type == 0:  # Create token command
#             tokens[token_id] = time + expiry_limit
#         elif cmd_type == 1 and token_id in tokens and tokens[token_id] >= time:  # Reset token command
#             tokens[token_id] = time + expiry_limit
    
#     # The maximum time T will be the time of the last command plus expiry_limit
#     max_time = commands[-1][2] + expiry_limit
#     # Count the tokens that are still active at max_time
#     active_tokens = sum(1 for expiry in tokens.values() if expiry >= max_time)
    
#     return active_tokens

# # Example usage:
# expiry_limit_example = 4
# commands_example = [[0, 1, 1], [0, 2, 2], [1, 1, 5], [1, 2, 7]]
# process_commands(expiry_limit_example, commands_example)


# ls = ['coding','decoding']
                
                       
             