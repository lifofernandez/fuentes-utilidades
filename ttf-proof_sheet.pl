use PDF::API2;
use strict;
use warnings;
use feature 'say';

my $builtin_txt = 'Hello World!';
my ($font_path, $txt) = @ARGV;


if (not defined $font_path) {
  say "'$0' needs some TTF file";
  exit;
}

# Create a blank PDF file
my $pdf = PDF::API2->new();

# Add a blank page
my $page = $pdf->page();

# Retrieve an existing page
#$page = $pdf->openpage($page_number);

# Set the page size
$page->mediabox('Letter');

# Add an external TTF font to the PDF
my $font = $pdf->ttfont($font_path);

# Add some text to the page
my $text = $page->text();
$text->font($font, 20);
$text->translate(200, 700);
if (not defined $txt) {
  say "No text file provided, using builtin dummy text";
  $text->text($builtin_txt);
}else{
  $text->text($txt);
}

# Save the PDF
$pdf->saveas($font_path.'.pdf');
