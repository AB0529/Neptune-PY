from discord.ext import commands
import discord, sys, ast, subprocess

# Owner category
class Owner(commands.Cog):
    def __init__(self, nep):
        self.nep = nep
        self.util = nep.get_cog('Utils')

    # -----------------------------------------------------------------

    # Kill command
    @commands.command(
        name='kill',
        aliases=['stop'],
        hidden=True,
        description='Logs bot out and kills process'
        )
    @commands.is_owner()
    async def kill(self, c):
        await c.send('Killing...')
        await self.nep.logout()

    # -----------------------------------------------------------------

    # Set status command
    @commands.command(
        name='status',
        aliases=['ss'],
        hidden=True,
        description='Logs bot out and kills process'
        )
    @commands.is_owner()
    async def status(self, c, _type='playing', *status):
        status = ' '.join(status)
        acceptable_tpyes = ['playing', 'watching', 'listening']

        # Make sure correct type is used
        if _type not in acceptable_tpyes:
            return await self.util.error(c, 'Invalid Args', f'`{_type}` is not an acceptable type!')
        
        # Set the activity
        await self.nep.change_presence(activity=discord.Activity(name=status, type=discord.ActivityType[_type.lower()]))
        await self.util.embed(c, f'✅ | Activity changed to `{_type.upper()} {status}`')

    # -----------------------------------------------------------------

    # Reload cog command
    @commands.command(
        name='reload',
        aliases=['re'],
        hidden=True,
        descrription='Reloads a specified cog'
    )
    @commands.is_owner()
    async def reload(self, c, cog):
        # Reload cog
        self.nep.reload_extension(f'Cogs.{cog.capitalize()}')
        await self.util.embed(c, f'🌀 | Cog `{cog}` has been reloaded')
    
    # -----------------------------------------------------------------

    # Eval command
    @commands.command(
        name='eval',
        aliases=['ev'],
        hidden=True,
        description='Evaluates Python code'
    )
    @commands.is_owner()
    async def eval(self, c, *, code):
        code = code.strip('` ')
        # Add indentation
        code = '\n'.join(f'    {i}' for i in code.splitlines())
        # Warp code 
        body = f'async def _eval_code_gamer():\n{code}'

        parsed = ast.parse(body)
        body = parsed.body[0].body

        # Allow for indents
        self.util.insert_returns(body)

        # Create environment
        env = {
            'bot': c.bot,
            'discord': discord,
            'commands': commands,
            'c': c,
            '__import__': __import__
        }

        # Compile code
        exec(compile(parsed, filename='<ast>', mode='exec'), env)
        result = (await eval(f"_eval_code_gamer()", env))

        # Send result
        await self.util.embed(c, f'🤖 | Eval Resulsts:\n```py\n{result}\n```')

    # -----------------------------------------------------------------

    # Exec command
    @commands.command(
        name='exec',
        aliases=['ex'],
        hidden=True,
        description='Execucutes Unix commands'
    )
    @commands.is_owner()
    async def exec(self, c, *, cmd='ls'):
        # Disable rm 
        if cmd[0] == 'rm':
            await c.send('No rm >:(')
        # Run command
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        # Get outputs
        (output, err) = proc.communicate()
        output = str(output).split('\\n')
        proc_status = proc.wait()
        nl = '\n'
        b = 'b\''

        await self.util.embed(c, f'💻 | Exec results:\n```\n{nl.join(output).replace(b, "")}\n\nStatus: {proc_status}\n```')

    # -----------------------------------------------------------------

def setup(nep):
    nep.add_cog(Owner(nep))