import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# .envファイルからトークンを読み込む
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # メッセージのコンテンツを読み取るためのintents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def userguard(ctx, *members: discord.Member):
    # "safeuser" という名前のロールを探す
    role = discord.utils.get(ctx.guild.roles, name="safeuser")
    
    # ロールが存在しない場合、新しく作成する
    if role is None:
        role = await ctx.guild.create_role(name="safeuser")
        await ctx.send("「safeuser」ロールを作成しました。")

    # 指定されたユーザーにロールを付与
    for member in members:
        if role in member.roles:
            await ctx.send(f"{member.mention} には既に「safeuser」ロールが付与されています。")
        else:
            await member.add_roles(role)
            await ctx.send(f"{member.mention} に「safeuser」ロールを付与しました。")

# Botのトークンを使って実行
bot.run(TOKEN)
