import discord, random, ast, os
from discord.ext import commands


# Utils cog
class Utils(commands.Cog):
    def __init__(self, nep):
        self.nep = nep
        self.r_color = random.randint(0, 0xffffff)

    # -----------------------------------------------------------------

    # Easy embed
    async def embed(self, c, content):
        embed = discord.Embed(description=content, color=self.r_color)
        await c.send(embed=embed)

    # -----------------------------------------------------------------

    # Easy error handle
    async def error(self, c, _type='Idfk', error='Error handler errored, wack'):
        await self.embed(c, f':x: Error | Oh nose, an **error occured**!\n```xl\nType: {_type}\n\n{error}\n```')

    # -----------------------------------------------------------------

    # Returns list of all cogs
    def get_all_cogs(self):
        cogs = [self.nep.get_cog(f'Cogs.{f.replace(".py", "")}') for f in os.listdir('Cogs') if not f.startswith('__')]

        return cogs

    # -----------------------------------------------------------------

    # Helper func for eval (https://github.com/nitros12)
    def insert_returns(self, body):
        # insert return stmt if the last expression is a expression statement
        if isinstance(body[-1], ast.Expr):
            body[-1] = ast.Return(body[-1].value)
            ast.fix_missing_locations(body[-1])

        # for if statements, we insert returns into the body and the orelse
        if isinstance(body[-1], ast.If):
            self.insert_returns(body[-1].body)
            self.insert_returns(body[-1].orelse)

        # for with blocks, again we insert returns into the body
        if isinstance(body[-1], ast.With):
            self.insert_returns(body[-1].body)

    # -----------------------------------------------------------------

    # Checks for correct flags
    def get_queue_flags(self, args, acceptable_flags):
        correct_flags = list(acceptable_flags.keys())
        aliases = [acceptable_flags[cf] for cf in correct_flags]

        print(correct_flags, aliases)

        if args in correct_flags or args in aliases:
            print('YEE')
            print(correct_flags, aliases)

            return correct_flags[args]

        # return f'-{args}' in correct_flags or map(lambda a: f'-{args}' in a, acceptable_flags[correct_flags])
        return False 

    # -----------------------------------------------------------------

def setup(nep):
    nep.add_cog(Utils(nep))
