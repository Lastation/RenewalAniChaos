import variable as v;
import func.trig as trg;
import func.trigepic as epic;

function buff(playerID)
{
   for (var i = 0; i < 6; i ++)
   {
      if (v.P_LawBuff[i] > 0)
      {
         trg.Buff_ShieldFixPlayer(i, 1);
         v.P_LawBuff[i] = v.P_LawBuff[i] - 1;
      }
   }
}

function main(playerID)
{
   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] == 0)
         {
            trg.Shape_Dot(playerID, 1, "40 + 1n Gantrithor", 0, 0);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", playerID);
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 4)
         {            
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         if (v.P_LoopMain[playerID] < 4)
         {
            epic.Shape_Edge(playerID, 1, "Protoss Observer", 45, 3 + 2 * v.P_LoopMain[playerID], 50 + 50 * v.P_LoopMain[playerID], 1);
            KillUnitAt(All, "Protoss Observer", "Anywhere", playerID);
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 4)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 2)
      {
         trg.ResizeLocation(playerID, 15, 15);
         MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");

         if (playerID < 3)
         {
            for (var i = 0; i < 3; i++)
            {
               if (Bring(i, AtLeast, 1, v.P_UnitID[i], v.P_LocationID[playerID]))
               {
                  v.P_LawBuff[i] = 96;
               }
            }
         }
         else if (playerID >= 3)
         {
            for (var i = 3; i < 6; i++)
            {
               if (Bring(i, AtLeast, 1, v.P_UnitID[i], v.P_LocationID[playerID]))
               {
                  v.P_LawBuff[i] = 96;
               }
            }
         }

         SetDeaths(playerID, SetTo, 720, " `UniqueCoolTime");
         trg.SkillEnd();
      }
   }
}