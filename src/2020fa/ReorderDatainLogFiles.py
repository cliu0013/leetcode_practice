class Solution:
    def reorderLogFiles(self, logs):
        digit_logs_list = []
        string_logs_list = []
        for log in logs:
            if (log.split()[1]).isdigit():
                digit_logs_list.append(log)
            else:
                string_logs_list.append(log)
        sorted_list = sorted(string_logs_list, key = lambda log: (log.split()[1:], log.split()[0]))
        sorted_list.extend(digit_logs_list)
        return sorted_list