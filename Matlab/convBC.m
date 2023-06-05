function conv = convBC(location, state, temperature)
%reads out current fire temperature from given temperature profile
time=round(state.time);
 if ~isnan(state.time)
    %assert(length(temperature) == length(t), "temperature time vector not equal to simulation time vector");
    conv = location.y;
%     alpha=10/1000000;
    try 
        if time == 0
            time = time+1;
        end
        conv(:)=temperature(time);
%         if time < 30*3600
%             alpha=0;
    catch 
        time
        return
    end
 else
     conv = nan(1, length(location.x));
 end
