frame = select from frames folder
base = base64.encode(frame)
result = model.input(base)
api.output(
    frame,
    result
)

