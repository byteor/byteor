%[ ��� ][ �ֶο�� ][. ��ȷ�� ][ �������η� ] ���η�

��ǣ�flags��:
 
 +   ������ǰ���һ���Ӻ�
 
 ' ' ������ǰ���һ���Ӻţ������Դ��� + ʹ�ã�
 
 -   ��������뵽�ֶ����
 
 0   �����ǰ�油��0��һֱ����ֵ��������Ϊֹ�������Դ���ʹ��-��
     ��������˵�����ָ����ȷ�ȣ������֮
 
 #   ʹ�������ת������������ʾ

     A��a��E��e��F��f��G��g
        ��С����Ϊ����������ʶ������С�������û������Ҳһ��

     G��g
        ��Ҫ�Ѻ����0�ض�
     
     X��x��o
        ǰ��0X��0x���Ը�ʽ����0��ʮ������������ǰ��0���Ը�ʽ���˽�������

===

printf()ת�����η������η�

���η�          ת�����η�             ��Ӧ���Ա�������

hh              d��i��o��u��x��X       signed char��unsigned char

hh              n                      singed char *

h               d��i��o��u��x��X       short int �� unsigned short int

h               n                      short int *

l����ĸL��      d��i��o��u��x��X       long int �� unsigned long int

l����ĸL��      c                      wint_t

l����ĸL��      n                      long int *

l����ĸL��      s                      wchar_t *

l����ĸL��      a��A��e��E��f��F��g��G ������ʹ�����η�����û�����ã�

ll��������ĸL�� d��i��o��u��x��X       long long �� unsigned long long 

ll��������ĸL�� n                      long long *

j               d��i��o��u��x��X       intmax_t �� uintmax_t

j               n                      intmax_t *

z               d��i��o��u��x��X       size_t ���Ӧ���з�����������

z               n                      size_t * ���� "ָ���з�����������"��ָ��

t               d��i��o��u��x��X       ptrdiff_t ���߶�Ӧ���޷�����������

t               n                      ptrdiff_t * ����"ָ���Ӧ�з�������"��ָ��

L               a��A��e��E��f��F��g��G long double

===

printf()ת�����η�

ת�����η�        �Ա�������                �������

d��i              int                       ʮ����

u                 unsigned int              ʮ����

o                 unsigned int              �˽���

x��X              unsigned int              ʮ������

f��F              float �� double           ʮ���Ƹ�����

e��E              float �� double           ָ��������

g��G              float �� double           ʮ���Ƹ������򸡵�������

a��A              float �� double           ʮ������ָ��������

c                 char �� int               ��һ�ַ�

s                 char *                    ָ���Ա�����ָ����ַ�������

n                 int *                     û�������printf()�Ὣ"ĿǰΪ
                                            ֹ������ַ�"�洢��"���Ա�����
                                            ָ��"�ı�����

p                 �κ�ָ������              ָ��ֵ(��ʮ�����Ƽ�������ʾ)

%                 û��                      �ٷֱȷ���(%)

===

������stdint.h�е�ת�����η���

����                ����                      printf()ת�����η�

intN_t              ���ΪNλ����������       PRIdN��PRIiN

uintN_t                                       PRIoN��PRIuN��PRIxN��PRIXN

int_leastN_t        �������ΪNλ����������   PRIdLEASTN��PRIiLEASTN

uint_leastN_t                                 PRIoLEASTN��PRIuLEASTN��
                                              PRIxLEASTN��PRIXLEASTN

int_fastN_t         �������Nλ               PRIdFASTN��PRIiFASTN

uint_fastN_t        �����ٶ�������������    PRIoFASTN��PRIuFASTN��
                                              PRIxFASTN��PRIXFASTN

intmax_t            ������������            PRIdMAX��PRIiMAX

uintmax_t                                     PRIoMAX��PRIuMAX��PRIxMAX��PRIXMAX

intptr_t            ���Դ洢ָ��ֵ����������  PRIdPTR��PRIiPTR

uintptr_t                                     PRIoPTR��PRIuPTR��PRIxPTR��PRIXPTR
