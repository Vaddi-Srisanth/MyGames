#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0;
    int cond=0,pos=0,player=0;
    char ar='1',br='2',cr='3',dr='4',er='5',fr='6',gr='7',hr='8',ir='9',let;

    while(1)
    {

        if(player % 2 == 0)
            let = 'x';
        else
            let = 'o';

        printf("\n");
        printf("%c | %c | %c\n", ar, br, cr);
        printf("--+---+--\n");
        printf("%c | %c | %c\n", dr, er, fr);
        printf("--+---+--\n");
        printf("%c | %c | %c\n", gr, hr, ir);

        printf("\nPlayer %c, enter position (1-9): ", let);
        scanf("%d",&pos);

        switch(pos)
        {
            case 1:
                if(a!=0){printf("Already occupied!\n"); continue;}
                a=1; ar=let;
                break;

            case 2:
                if(b!=0){printf("Already occupied!\n"); continue;}
                b=1; br=let;
                break;

            case 3:
                if(c!=0){printf("Already occupied!\n"); continue;}
                c=1; cr=let;
                break;

            case 4:
                if(d!=0){printf("Already occupied!\n"); continue;}
                d=1; dr=let;
                break;

            case 5:
                if(e!=0){printf("Already occupied!\n"); continue;}
                e=1; er=let;
                break;

            case 6:
                if(f!=0){printf("Already occupied!\n"); continue;}
                f=1; fr=let;
                break;

            case 7:
                if(g!=0){printf("Already occupied!\n"); continue;}
                g=1; gr=let;
                break;

            case 8:
                if(h!=0){printf("Already occupied!\n"); continue;}
                h=1; hr=let;
                break;

            case 9:
                if(i!=0){printf("Already occupied!\n"); continue;}
                i=1; ir=let;
                break;

            default:
                printf("Invalid position!\n");
                continue;
        }
        if((ar==br && br==cr) ||
           (dr==er && er==fr) ||
           (gr==hr && hr==ir) ||
           (ar==dr && dr==gr) ||
           (br==er && er==hr) ||
           (cr==fr && fr==ir) ||
           (ar==er && er==ir) ||
           (cr==er && er==gr))
        {
            printf("\n");
            printf("%c | %c | %c\n", ar, br, cr);
            printf("--+---+--\n");
            printf("%c | %c | %c\n", dr, er, fr);
            printf("--+---+--\n");
            printf("%c | %c | %c\n", gr, hr, ir);

            printf("\nPlayer %c wins!\n", let);
            break;
        }

        cond = a+b+c+d+e+f+g+h+i;

        if(cond == 9)
        {
            printf("\n");
            printf("%c | %c | %c\n", ar, br, cr);
            printf("--+---+--\n");
            printf("%c | %c | %c\n", dr, er, fr);
            printf("--+---+--\n");
            printf("%c | %c | %c\n", gr, hr, ir);

            printf("\nIt's a draw!\n");
            break;
        }

        player++;
    }

    return 0;
}