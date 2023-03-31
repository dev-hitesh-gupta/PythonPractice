import click

def process_file(input_file, output_file, encrypt):
    """Process a file."""
    try:
        data = input_file.read()
    except IOError as e:
        raise click.BadParameter(f"Error reading input file: {e}")

    if encrypt:
        processed_data = bytes([byte ^ 0xff for byte in data])
    else:
        processed_data = bytes([byte ^ 0x00 for byte in data])

    try:
        output_file.write(processed_data)
    except IOError as e:
        raise click.BadParameter(f"Error writing to output file: {e}")

@click.group()
def cli():
    pass

@cli.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    """Print a greeting."""
    for _ in range(count):
        click.echo(f'Hello, {name}!')

@cli.command()
@click.argument('input_file', type=click.Path(exists=True, dir_okay=False))
@click.argument('output_file', type=click.Path(writable=True, dir_okay=False))
@click.option('--encrypt/--decrypt', default=True, help='Encrypt or decrypt the input file.')
def process(input_file, output_file, encrypt):
    """Process a file."""
    try:
        with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
            process_file(f_in, f_out, encrypt)
    except (IOError, ValueError) as e:
        raise click.BadParameter(f"Error processing file: {e}")

if __name__ == '__main__':
    cli()
