#!/usr/bin/perl
use strict;
use warnings FATAL => 'all';

my $file = $ARGV[0] or die "Need to get CSV file on the command line\n";
my $sum = 0;
open(my $data, '<', $file) or die "Could not open '$file' $!\n";

while (my $line = <$data>) {
    chomp $line;
    my @numbers = split "," , $line;
    addNUmbers(@numbers)
}

sub addNUmbers {
    my @numbers = (@_);
    while(my $number = <@numbers>){
        $sum += $number;
    }
}
print($sum);

while(my $var = <array to traverse>){

    }