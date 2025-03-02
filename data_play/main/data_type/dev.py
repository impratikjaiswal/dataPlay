from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys

from data_play.main.data_type.data_type_master import DataTypeMaster
from data_play.main.helper.data import Data

sample_java_code_1 = """
package amenitypj.cardtools.api.util;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 * Offers various conversion methods.
 */
public class Converter
{
    private static boolean hexInCaps;

    private static short counterForByteArray;

    /**
     * Instantiates a new converter.
     */
    Converter( )
    {
    }

    /**
     * Change hex case.
     *
     * @param str
     *            the str
     * @return the string
     */
    private static String changeHexCase( String str )
    {
        return ( hexInCaps ? str.toUpperCase() : str );
    }

    public static String insertBlanks( String source, int n )
    {
        String dest = Constants.STR_BLANK;
        for ( int i = 0; i <= source.length() - n; i += n )
        {
            dest += source.substring( i, i + n ) + Constants.STR_SPACE;
        }
        return dest.trim();
    }

    public static String toHexString( char[] ca, boolean withSpace, int n )
    {
        if ( ca == null )
        {
            return Constants.STR_BLANK;
        }
        else
        {
            String s = Constants.STR_BLANK;
            int toConvert = Math.min( n, ca.length );
            for ( int i = 0; i < toConvert; i++ )
            {
                s += changeHexCase( hexAlign( (short)ca[ i ], 1 ) );
                if ( withSpace )
                {
                    s += Constants.STR_SPACE;
                }
            }
            return s.trim();
        }
    }

    public static String toHexString( char[] ca, boolean withSpace ) {
        if ( ca == null ) {
            return Constants.STR_BLANK;
        }
        else 
        {
            return ( toHexString( ca, withSpace, ca.length ) );
        }
        return Constants.STR_BLANK;
    }

    public static String toHexString( char[] ca )
    {
        if ( ca == null )
        {
            return Constants.STR_BLANK;
        }
        else
        {
            return ( toHexString( ca, true, ca.length ) );
        }
        return Constants.STR_BLANK;
    }

    public static byte toByte( byte nibbleFirst, byte nibbleSecond )
    {
        return (byte) ( nibbleFirst | nibbleSecond );
    }

    public static String toString( Object[] objArray, char charSeparator ) {
        return toString( (String[])objArray, Constants.STR_BLANK + charSeparator );
    }

    public static String toString( Object[] objArray, String strSeparator ) {
        return toString( (String[])objArray, strSeparator );
    }

    public static String toString( String[] strArray, char charSeparator )
    {
        return toString( strArray, Constants.STR_BLANK + charSeparator );
    }

    public static String toString( char value ) {
        return "" + value;
    }
}"""

sample_groovy_code_1 = """
package amenitypj.cardtools.api.util;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 * Offers various conversion methods.
 */
    private static boolean hexInCaps;

    private static short counterForByteArray;

    /**
     * Instantiates a new converter.
     */
    Converter( )
    {
    }

    /**
     * Change hex case.
     *
     * @param str
     *            the str
     * @return the string
     */
    private static String changeHexCase( String str )
    {
        return ( hexInCaps ? str.toUpperCase() : str );
    }

    public static String insertBlanks( String source, int n )
    {
        String dest = Constants.STR_BLANK;
        for ( int i = 0; i <= source.length() - n; i += n )
        {
            dest += source.substring( i, i + n ) + Constants.STR_SPACE;
        }
        return dest.trim();
    }

    public static String toHexString( char[] ca, boolean withSpace, int n )
    {
        if ( ca == null )
        {
            return Constants.STR_BLANK;
        }
        else
        {
            String s = Constants.STR_BLANK;
            int toConvert = Math.min( n, ca.length );
            for ( int i = 0; i < toConvert; i++ )
            {
                s += changeHexCase( hexAlign( (short)ca[ i ], 1 ) );
                if ( withSpace )
                {
                    s += Constants.STR_SPACE;
                }
            }
            return s.trim();
        }
    }

    public static String toHexString( char[] ca, boolean withSpace ) {
        if ( ca == null ) {
            return Constants.STR_BLANK;
        }
        else 
        {
            return ( toHexString( ca, withSpace, ca.length ) );
        }
        return Constants.STR_BLANK;
    }

    public static String toHexString( char[] ca )
    {
        if ( ca == null )
        {
            return Constants.STR_BLANK;
        }
        else
        {
            return ( toHexString( ca, true, ca.length ) );
        }
        return Constants.STR_BLANK;
    }

    public static byte toByte( byte nibbleFirst, byte nibbleSecond )
    {
        return (byte) ( nibbleFirst | nibbleSecond );
    }

    public static String toString( Object[] objArray, char charSeparator ) {
        return toString( (String[])objArray, Constants.STR_BLANK + charSeparator );
    }

    public static String toString( Object[] objArray, String strSeparator ) {
        return toString( (String[])objArray, strSeparator );
    }

    public static String toString( String[] strArray, char charSeparator )
    {
        return toString( strArray, Constants.STR_BLANK + charSeparator );
    }

    public static String toString( char value ) {
        return "" + value;
    }
"""


class Dev(DataTypeMaster):

    def __init__(self):
        super().__init__()

    def set_print_input(self):
        print_input = None
        super().set_print_input(print_input)

    def set_print_output(self):
        print_output = None
        super().set_print_output(print_output)

    def set_print_info(self):
        print_info = None
        super().set_print_info(print_info)

    def set_quiet_mode(self):
        quite_mode = None
        super().set_quiet_mode(quite_mode)

    def set_remarks(self):
        remarks = None
        super().set_remarks(remarks)

    def set_encoding(self):
        encoding = None
        super().set_encoding(encoding)

    def set_encoding_errors(self):
        encoding_errors = None
        super().set_encoding_errors(encoding_errors)

    def set_output_path(self):
        output_path = None
        super().set_output_path(output_path)

    def set_output_file_name_keyword(self):
        output_file_name_keyword = None
        super().set_output_file_name_keyword(output_file_name_keyword)

    def set_archive_output(self):
        archive_output = None
        super().set_archive_output(archive_output)

    def set_archive_output_format(self):
        archive_output_format = None
        super().set_archive_output_format(archive_output_format)

    def set_content_mappings(self):
        content_mappings = None
        super().set_content_mappings(content_mappings)

    def set_name_mappings(self):
        name_mappings = None
        super().set_name_mappings(name_mappings)

    def set_data_pool(self):
        data_pool = [
            #
            Data(
                remarks='Sample Java Code',
                input_data=sample_java_code_1,
                content_mappings=[
                    {
                        PhKeys.INCLUDE_SEARCH_PATTERN: 'String toHexString',
                        PhKeys.INCLUDE_START_BLOCK_PATTERN: PhConstants.STR_CURLY_BRACE_START,
                        PhKeys.INCLUDE_END_BLOCK_PATTERN: PhConstants.STR_CURLY_BRACE_END,
                        PhKeys.DELETE_BLOCK: PhConstants.UNKNOWN,
                    }
                ]
            ),
            #
            Data(
                remarks='Sample Groovy Code',
                input_data=sample_groovy_code_1,
                content_mappings=[
                    {
                        PhKeys.INCLUDE_SEARCH_PATTERN: 'String toHexString',
                        PhKeys.INCLUDE_START_BLOCK_PATTERN: PhConstants.STR_CURLY_BRACE_START,
                        PhKeys.INCLUDE_END_BLOCK_PATTERN: PhConstants.STR_CURLY_BRACE_END,
                        PhKeys.DELETE_BLOCK: PhConstants.UNKNOWN,
                    }
                ]
            ),
            # #
            # Data(
            #     remarks='Sample Java Code',
            #     input_data=sample_java_code_1,
            #     content_mappings=[
            #         {'brown': 'black'},
            #         {'dog': 'cat'},
            #     ]
            # ),
            #
        ]
        super().set_data_pool(data_pool)
