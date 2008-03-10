import org.puremvc.python.interfaces
import org.puremvc.python.patterns.observer

class MacroCommand( org.puremvc.python.patterns.observer.Notifier, org.puremvc.python.interfaces.ICommand, org.puremvc.python.interfaces.INotifier ):
    """
    A base C{ICommand} implementation that executes other C{ICommand}s.
     
    A C{MacroCommand} maintains an list of
    C{ICommand} Class references called I{SubCommands}.
    
    When C{execute} is called, the C{MacroCommand} 
    instantiates and calls C{execute} on each of its I{SubCommands} turn.
    Each I{SubCommand} will be passed a reference to the original
    C{INotification} that was passed to the C{MacroCommand}'s 
    C{execute} method.

    Unlike C{SimpleCommand}, your subclass
    should not override C{execute}, but instead, should 
    override the C{initializeMacroCommand} method, 
    calling C{addSubCommand} once for each I{SubCommand}
    to be executed.
    
    @see org.puremvc.core.controller.Controller Controller
    @see org.puremvc.patterns.observer.Notification Notification
    @see org.puremvc.patterns.command.SimpleCommand SimpleCommand
    """
    __subCommands = None
    
    def __init__( self ):
        """
        Constructor. 
        
        You should not need to define a constructor, 
        instead, override the C{initializeMacroCommand}
        method.

        If your subclass does define a constructor, be 
        sure to call C{super()}.
        """
        self.__subCommands = ()
        self.initializeMacroCommand()
    
    def initializeMacroCommand( self ):
        """
        Initialize the C{MacroCommand}.
        
        In your subclass, override this method to 
        initialize the C{MacroCommand}'s I{SubCommand}  
        list with C{ICommand} class references like 
        this:
        
        C{
            # Initialize MyMacroCommand
            def initializeMacroCommand( self ):
                addSubCommand( com.me.myapp.controller.FirstCommand )
                addSubCommand( com.me.myapp.controller.SecondCommand )
                addSubCommand( com.me.myapp.controller.ThirdCommand )

        }
        
        Note that I{SubCommand}s may be any C{ICommand} implementor,
        C{MacroCommand}s or C{SimpleCommands} are both acceptable.
        """
        pass
    
    def addSubCommand( self, commandClassRef ):
        """
        Add a I{SubCommand}.

        The I{SubCommands} will be called in First In/First Out (FIFO)
        order.
         
        @param commandClassRef: a reference to the C{Class} of the C{ICommand}.
        """
        self.subCommands.append( commandClassRef )
    
    def execute( self, notification ):
        """
        Execute this C{MacroCommand}'s I{SubCommands{.
        
        The I{SubCommands} will be called in First In/First Out (FIFO)
        order. 
        
        @param notification the C{INotification} object to be passsed to each I{SubCommand}.

        """
        while len( self.__subCommands ) > 0:
            commandClassRef = self.__subCommands.pop()
            commandInstance = eval( commandClassRef )()
            commandInstance.execute( notification )

class SimpleCommand( org.puremvc.python.patterns.observer.Notifier, org.puremvc.python.interfaces.ICommand, org.puremvc.python.interfaces.INotifier ):
    """
    A base C{ICommand} implementation.
    
    Your subclass should override the C{execute} 
    method where your business logic will handle the C{INotification}.
    
    @see org.puremvc.core.controller.Controller Controller
    @see org.puremvc.patterns.observer.Notification Notification
    @see org.puremvc.patterns.command.MacroCommand MacroCommand
    """
    
    def execute( self, notification ):
        """
        Fulfill the use-case initiated by the given C{INotification}.
        
        In the Command Pattern, an application use-case typically
        begins with some user action, which results in an C{INotification} being broadcast, which 
        is handled by business logic in the C{execute} method of an
        C{ICommand}.
        
        @param notification: the C{INotification} to handle.
        """
        pass