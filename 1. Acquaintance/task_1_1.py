def convert_time(duration: int) -> str:
    seconds = duration % 60
    minutes = duration // 60 % 60
    hours = duration // (60 * 60) % 60 % 24
    days = duration // (60 * 60 * 24)
    if duration < 60:
        return f'{seconds} sec.'
    elif duration < 60 * 60:
        return f'{minutes} min / {seconds} sec.'
    elif duration < 60 * 60 * 24:
        return f'{hours} hours / {minutes} min / {seconds} sec.'
    else:
        return f'{days} days / {hours} hours / {minutes} min / {seconds} sec.'

duration = 45634456
result = convert_time(duration)
print(result)

