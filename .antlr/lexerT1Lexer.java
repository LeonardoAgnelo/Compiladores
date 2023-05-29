// Generated from c:\u005Cufscar\Compiladores\T1\lexerT1.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class lexerT1Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		KEYWORDS=1, OP_REL=2, OP_ARITH=3, OP_LOGIC=4, NUM_INT=5, NUM_REAL=6, IDENT=7, 
		CADEIA=8, PARENTHESES=9, SQUARE_BRACKETS=10, REANGE=11, ATTRIBUTE=12, 
		DELIMIT=13, SEPARETOR=14, ATRIBUITION=15, ADDRESS=16, POINTER=17, COMMENT=18, 
		WHITE_SPACE=19;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"KEYWORDS", "OP_REL", "OP_ARITH", "OP_LOGIC", "NUM_INT", "NUM_REAL", 
			"IDENT", "CADEIA", "PARENTHESES", "SQUARE_BRACKETS", "REANGE", "ATTRIBUTE", 
			"DELIMIT", "SEPARETOR", "ATRIBUITION", "ADDRESS", "POINTER", "COMMENT", 
			"WHITE_SPACE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, "'..'", 
			"'.'", "':'", "','", "'<-'", "'&'", "'^'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "KEYWORDS", "OP_REL", "OP_ARITH", "OP_LOGIC", "NUM_INT", "NUM_REAL", 
			"IDENT", "CADEIA", "PARENTHESES", "SQUARE_BRACKETS", "REANGE", "ATTRIBUTE", 
			"DELIMIT", "SEPARETOR", "ATRIBUITION", "ADDRESS", "POINTER", "COMMENT", 
			"WHITE_SPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public lexerT1Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "lexerT1.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25\u0174\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\5\2\u0119\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u0124\n\3\3\4"+
		"\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u012e\n\5\3\6\6\6\u0131\n\6\r\6\16\6"+
		"\u0132\3\7\3\7\3\7\3\7\3\b\3\b\7\b\u013b\n\b\f\b\16\b\u013e\13\b\3\b\5"+
		"\b\u0141\n\b\3\b\7\b\u0144\n\b\f\b\16\b\u0147\13\b\3\t\3\t\7\t\u014b\n"+
		"\t\f\t\16\t\u014e\13\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3"+
		"\16\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\7\23\u0168"+
		"\n\23\f\23\16\23\u016b\13\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\2"+
		"\2\25\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35"+
		"\20\37\21!\22#\23%\24\'\25\3\2\n\6\2\'\',-//\61\61\3\2\62;\4\2C\\c|\5"+
		"\2\62;C\\c|\5\2\f\f\17\17$$\4\2]]__\6\2\f\f\17\17}}\177\177\5\2\13\f\17"+
		"\17\"\"\2\u01a1\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3"+
		"\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2"+
		"\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3"+
		"\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3\u0118\3\2\2\2\5\u0123\3\2\2"+
		"\2\7\u0125\3\2\2\2\t\u012d\3\2\2\2\13\u0130\3\2\2\2\r\u0134\3\2\2\2\17"+
		"\u0138\3\2\2\2\21\u0148\3\2\2\2\23\u0151\3\2\2\2\25\u0153\3\2\2\2\27\u0155"+
		"\3\2\2\2\31\u0158\3\2\2\2\33\u015a\3\2\2\2\35\u015c\3\2\2\2\37\u015e\3"+
		"\2\2\2!\u0161\3\2\2\2#\u0163\3\2\2\2%\u0165\3\2\2\2\'\u0170\3\2\2\2)*"+
		"\7c\2\2*+\7n\2\2+,\7i\2\2,-\7q\2\2-.\7t\2\2./\7k\2\2/\60\7v\2\2\60\61"+
		"\7o\2\2\61\u0119\7q\2\2\62\63\7h\2\2\63\64\7k\2\2\64\65\7o\2\2\65\66\7"+
		"a\2\2\66\67\7c\2\2\678\7n\2\289\7i\2\29:\7q\2\2:;\7t\2\2;<\7k\2\2<=\7"+
		"v\2\2=>\7o\2\2>\u0119\7q\2\2?@\7f\2\2@A\7g\2\2AB\7e\2\2BC\7n\2\2CD\7c"+
		"\2\2DE\7t\2\2E\u0119\7g\2\2FG\7n\2\2GH\7k\2\2HI\7v\2\2IJ\7g\2\2JK\7t\2"+
		"\2KL\7c\2\2L\u0119\7n\2\2MN\7k\2\2NO\7p\2\2OP\7v\2\2PQ\7g\2\2QR\7k\2\2"+
		"RS\7t\2\2S\u0119\7q\2\2TU\7n\2\2UV\7g\2\2VW\7k\2\2W\u0119\7c\2\2XY\7g"+
		"\2\2YZ\7u\2\2Z[\7e\2\2[\\\7t\2\2\\]\7g\2\2]^\7x\2\2^\u0119\7c\2\2_`\7"+
		"t\2\2`a\7g\2\2ab\7c\2\2b\u0119\7n\2\2cd\7n\2\2de\7q\2\2ef\7i\2\2fg\7k"+
		"\2\2gh\7e\2\2h\u0119\7q\2\2ij\7g\2\2jk\7p\2\2kl\7s\2\2lm\7w\2\2mn\7c\2"+
		"\2no\7p\2\2op\7v\2\2p\u0119\7q\2\2qr\7h\2\2rs\7k\2\2st\7o\2\2tu\7a\2\2"+
		"uv\7g\2\2vw\7p\2\2wx\7s\2\2xy\7w\2\2yz\7c\2\2z{\7p\2\2{|\7v\2\2|\u0119"+
		"\7q\2\2}~\7u\2\2~\u0119\7g\2\2\177\u0080\7g\2\2\u0080\u0081\7p\2\2\u0081"+
		"\u0082\7v\2\2\u0082\u0083\7c\2\2\u0083\u0119\7q\2\2\u0084\u0085\7u\2\2"+
		"\u0085\u0086\7g\2\2\u0086\u0087\7p\2\2\u0087\u0088\7c\2\2\u0088\u0119"+
		"\7q\2\2\u0089\u008a\7h\2\2\u008a\u008b\7k\2\2\u008b\u008c\7o\2\2\u008c"+
		"\u008d\7a\2\2\u008d\u008e\7u\2\2\u008e\u0119\7g\2\2\u008f\u0090\7e\2\2"+
		"\u0090\u0091\7c\2\2\u0091\u0092\7u\2\2\u0092\u0119\7q\2\2\u0093\u0094"+
		"\7u\2\2\u0094\u0095\7g\2\2\u0095\u0096\7l\2\2\u0096\u0119\7c\2\2\u0097"+
		"\u0098\7h\2\2\u0098\u0099\7k\2\2\u0099\u009a\7o\2\2\u009a\u009b\7a\2\2"+
		"\u009b\u009c\7e\2\2\u009c\u009d\7c\2\2\u009d\u009e\7u\2\2\u009e\u0119"+
		"\7q\2\2\u009f\u00a0\7r\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2\7t\2\2\u00a2"+
		"\u0119\7c\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5\7v\2\2\u00a5\u0119\7g\2\2"+
		"\u00a6\u00a7\7h\2\2\u00a7\u00a8\7c\2\2\u00a8\u00a9\7e\2\2\u00a9\u0119"+
		"\7c\2\2\u00aa\u00ab\7h\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad\7o\2\2\u00ad"+
		"\u00ae\7a\2\2\u00ae\u00af\7r\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1\7t\2\2"+
		"\u00b1\u0119\7c\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5"+
		"\7i\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7\7u\2\2\u00b7\u00b8\7v\2\2\u00b8"+
		"\u00b9\7t\2\2\u00b9\u0119\7q\2\2\u00ba\u00bb\7h\2\2\u00bb\u00bc\7k\2\2"+
		"\u00bc\u00bd\7o\2\2\u00bd\u00be\7a\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0"+
		"\7g\2\2\u00c0\u00c1\7i\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3\7u\2\2\u00c3"+
		"\u00c4\7v\2\2\u00c4\u00c5\7t\2\2\u00c5\u0119\7q\2\2\u00c6\u00c7\7v\2\2"+
		"\u00c7\u00c8\7k\2\2\u00c8\u00c9\7r\2\2\u00c9\u0119\7q\2\2\u00ca\u00cb"+
		"\7r\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7e\2\2\u00ce"+
		"\u00cf\7g\2\2\u00cf\u00d0\7f\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2\7o\2\2"+
		"\u00d2\u00d3\7g\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7v\2\2\u00d5\u0119"+
		"\7q\2\2\u00d6\u00d7\7x\2\2\u00d7\u00d8\7c\2\2\u00d8\u0119\7t\2\2\u00d9"+
		"\u00da\7h\2\2\u00da\u00db\7k\2\2\u00db\u00dc\7o\2\2\u00dc\u00dd\7a\2\2"+
		"\u00dd\u00de\7r\2\2\u00de\u00df\7t\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1"+
		"\7e\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3\7f\2\2\u00e3\u00e4\7k\2\2\u00e4"+
		"\u00e5\7o\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8\7v\2\2"+
		"\u00e8\u0119\7q\2\2\u00e9\u00ea\7h\2\2\u00ea\u00eb\7w\2\2\u00eb\u00ec"+
		"\7p\2\2\u00ec\u00ed\7e\2\2\u00ed\u00ee\7c\2\2\u00ee\u0119\7q\2\2\u00ef"+
		"\u00f0\7t\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7q\2\2"+
		"\u00f3\u00f4\7t\2\2\u00f4\u00f5\7p\2\2\u00f5\u0119\7g\2\2\u00f6\u00f7"+
		"\7h\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7o\2\2\u00f9\u00fa\7a\2\2\u00fa"+
		"\u00fb\7h\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7e\2\2"+
		"\u00fe\u00ff\7c\2\2\u00ff\u0119\7q\2\2\u0100\u0101\7e\2\2\u0101\u0102"+
		"\7q\2\2\u0102\u0103\7p\2\2\u0103\u0104\7u\2\2\u0104\u0105\7v\2\2\u0105"+
		"\u0106\7c\2\2\u0106\u0107\7p\2\2\u0107\u0108\7v\2\2\u0108\u0119\7g\2\2"+
		"\u0109\u010a\7h\2\2\u010a\u010b\7c\2\2\u010b\u010c\7n\2\2\u010c\u010d"+
		"\7u\2\2\u010d\u0119\7q\2\2\u010e\u010f\7x\2\2\u010f\u0110\7g\2\2\u0110"+
		"\u0111\7t\2\2\u0111\u0112\7f\2\2\u0112\u0113\7c\2\2\u0113\u0114\7f\2\2"+
		"\u0114\u0115\7g\2\2\u0115\u0116\7k\2\2\u0116\u0117\7t\2\2\u0117\u0119"+
		"\7q\2\2\u0118)\3\2\2\2\u0118\62\3\2\2\2\u0118?\3\2\2\2\u0118F\3\2\2\2"+
		"\u0118M\3\2\2\2\u0118T\3\2\2\2\u0118X\3\2\2\2\u0118_\3\2\2\2\u0118c\3"+
		"\2\2\2\u0118i\3\2\2\2\u0118q\3\2\2\2\u0118}\3\2\2\2\u0118\177\3\2\2\2"+
		"\u0118\u0084\3\2\2\2\u0118\u0089\3\2\2\2\u0118\u008f\3\2\2\2\u0118\u0093"+
		"\3\2\2\2\u0118\u0097\3\2\2\2\u0118\u009f\3\2\2\2\u0118\u00a3\3\2\2\2\u0118"+
		"\u00a6\3\2\2\2\u0118\u00aa\3\2\2\2\u0118\u00b2\3\2\2\2\u0118\u00ba\3\2"+
		"\2\2\u0118\u00c6\3\2\2\2\u0118\u00ca\3\2\2\2\u0118\u00d6\3\2\2\2\u0118"+
		"\u00d9\3\2\2\2\u0118\u00e9\3\2\2\2\u0118\u00ef\3\2\2\2\u0118\u00f6\3\2"+
		"\2\2\u0118\u0100\3\2\2\2\u0118\u0109\3\2\2\2\u0118\u010e\3\2\2\2\u0119"+
		"\4\3\2\2\2\u011a\u0124\7@\2\2\u011b\u011c\7@\2\2\u011c\u0124\7?\2\2\u011d"+
		"\u0124\7>\2\2\u011e\u011f\7>\2\2\u011f\u0124\7?\2\2\u0120\u0121\7>\2\2"+
		"\u0121\u0124\7@\2\2\u0122\u0124\7?\2\2\u0123\u011a\3\2\2\2\u0123\u011b"+
		"\3\2\2\2\u0123\u011d\3\2\2\2\u0123\u011e\3\2\2\2\u0123\u0120\3\2\2\2\u0123"+
		"\u0122\3\2\2\2\u0124\6\3\2\2\2\u0125\u0126\t\2\2\2\u0126\b\3\2\2\2\u0127"+
		"\u012e\7g\2\2\u0128\u0129\7q\2\2\u0129\u012e\7w\2\2\u012a\u012b\7p\2\2"+
		"\u012b\u012c\7c\2\2\u012c\u012e\7q\2\2\u012d\u0127\3\2\2\2\u012d\u0128"+
		"\3\2\2\2\u012d\u012a\3\2\2\2\u012e\n\3\2\2\2\u012f\u0131\t\3\2\2\u0130"+
		"\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2"+
		"\2\2\u0133\f\3\2\2\2\u0134\u0135\5\13\6\2\u0135\u0136\7\60\2\2\u0136\u0137"+
		"\5\13\6\2\u0137\16\3\2\2\2\u0138\u013c\t\4\2\2\u0139\u013b\t\5\2\2\u013a"+
		"\u0139\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d\3\2"+
		"\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3\2\2\2\u013f\u0141\7a\2\2\u0140"+
		"\u013f\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0145\3\2\2\2\u0142\u0144\t\5"+
		"\2\2\u0143\u0142\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145"+
		"\u0146\3\2\2\2\u0146\20\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u014c\7$\2\2"+
		"\u0149\u014b\n\6\2\2\u014a\u0149\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a"+
		"\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014f\3\2\2\2\u014e\u014c\3\2\2\2\u014f"+
		"\u0150\7$\2\2\u0150\22\3\2\2\2\u0151\u0152\4*+\2\u0152\24\3\2\2\2\u0153"+
		"\u0154\t\7\2\2\u0154\26\3\2\2\2\u0155\u0156\7\60\2\2\u0156\u0157\7\60"+
		"\2\2\u0157\30\3\2\2\2\u0158\u0159\7\60\2\2\u0159\32\3\2\2\2\u015a\u015b"+
		"\7<\2\2\u015b\34\3\2\2\2\u015c\u015d\7.\2\2\u015d\36\3\2\2\2\u015e\u015f"+
		"\7>\2\2\u015f\u0160\7/\2\2\u0160 \3\2\2\2\u0161\u0162\7(\2\2\u0162\"\3"+
		"\2\2\2\u0163\u0164\7`\2\2\u0164$\3\2\2\2\u0165\u0169\7}\2\2\u0166\u0168"+
		"\n\b\2\2\u0167\u0166\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167\3\2\2\2\u0169"+
		"\u016a\3\2\2\2\u016a\u016c\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u016d\7\177"+
		"\2\2\u016d\u016e\3\2\2\2\u016e\u016f\b\23\2\2\u016f&\3\2\2\2\u0170\u0171"+
		"\t\t\2\2\u0171\u0172\3\2\2\2\u0172\u0173\b\24\2\2\u0173(\3\2\2\2\16\2"+
		"\u0118\u0123\u012d\u0132\u013a\u013c\u0140\u0143\u0145\u014c\u0169\3\b"+
		"\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}