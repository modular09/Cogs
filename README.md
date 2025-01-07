> [!TIP]
> You may use this one-liner cog file loader, must have also imported `os` package and be under `on_ready` function:
> ```py
> # Change './cogs' with your cog directory path.
> [await bot.load_extension(f'cogs.{entry.name[:-3]}') if entry.name.endswith('.py') else None for entry in os.scandir('./cogs')]
> ```
