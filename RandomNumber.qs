import Std.Diagnostics.DumpMachine;
import Std.Measurement.*;
import Std.Intrinsic.*;

operation Main() : Result[] {
    let nBits = 50;
    return GenerateNRandomBits(nBits);
}


operation GenerateNRandomBits(nBits : Int) : Result[] {

    use register = Qubit[nBits];

    for qubits in register {
        H(qubits);
    }

    let results = MResetEachZ(register);
    return results;
}