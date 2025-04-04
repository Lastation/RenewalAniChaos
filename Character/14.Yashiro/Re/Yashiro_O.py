import variable as v;
import func.trig as trg;

function main(playerID)
{
   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] == 0)
         {          
            trg.Shape_Dot(playerID, 1, "40 + 1n Wraith", 0, 0);

            KillUnitAt(All,  "40 + 1n Wraith", "Anywhere", playerID);

            trg.ResizeLocation(playerID, 15, 15);

            if (playerID < 3)
            {
               for (var i = 3; i < 6; i++)
               { 
                  if (Bring(i, AtLeast, 1, v.P_UnitID[i], v.P_LocationID[playerID]))
                  {
                     trg.Debuff_BanReturnPlayer(i);
                  }
               }
            }
            else
            {
               for (var i = 0; i < 3; i++)
               { 
                  if (Bring(i, AtLeast, 1, v.P_UnitID[i], v.P_LocationID[playerID]))
                  {
                     trg.Debuff_BanReturnPlayer(i);
                  }
               }
            }
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 1)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {      
         SetDeaths(playerID, SetTo, 2160, " `UniqueCoolTime");
      
         trg.SkillEnd();
      }
   }
}